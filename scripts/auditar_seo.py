"""Verifica o HTML gerado pelo Jekyll sem dependências externas."""
import argparse
from collections import Counter, defaultdict, deque
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.meta = {}
        self.canonicals, self.alternates, self.links, self.headings, self.graphs = [], [], [], [], []
        self.ids = set()
        self.lang = self.title = self.capture = ""
        self.feed(path.read_text(encoding="utf-8-sig"))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            self.capture = "title"
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href", ""))
        elif tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"):
            self.alternates.append((a["hreflang"], a.get("href", "")))
        elif tag == "meta":
            name = a.get("name") or a.get("property")
            if name:
                self.meta[name] = a.get("content", "")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.capture = "script"
            self.graphs.append("")
        elif tag in {"a", "img"}:
            address = a.get("href" if tag == "a" else "src")
            if address:
                self.links.append((tag, address, self.getpos()[0]))
        elif re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))

    def handle_endtag(self, tag):
        if self.capture == tag:
            self.capture = ""

    def handle_data(self, data):
        if self.capture == "title":
            self.title += data
        elif self.capture == "script":
            self.graphs[-1] += data


def trim_index(address):
    return address[:-10] if address.endswith("/index.html") else address


def audit(root, source, base):
    findings = []

    def report(level, rule, url, detail, line=None):
        findings.append(dict(severity=level, rule=rule, url=url, detail=detail, line=line))

    pages = {trim_index("/" + p.relative_to(root).as_posix()): Page(p) for p in root.rglob("*.html")}
    locales = json.loads((source / "_data/seo_locales.json").read_text(encoding="utf-8"))
    expected = defaultdict(dict)
    sources = list((source / "_posts").glob("*.md")) + list(source.glob("*.html"))
    for lang in locales.keys() - {"pt-BR"}:
        sources.extend((source / lang).glob("*.html"))
    for path in sources:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        if not content.startswith("---\n"):
            continue
        header = content[4:].split("\n---", 1)[0]
        meta = {key: value.strip().strip(chr(34) + chr(39)) for key, value in re.findall(r"(?m)^(translation_id|lang|permalink):[ \t]*(.+)$", header)}
        if "translation_id" not in meta:
            continue
        group, lang = meta["translation_id"], meta.get("lang", "")
        url = meta.get("permalink", "/" if path == source / "index.html" else "").strip("\"'")
        if not url or lang in expected[group]:
            report("error", "duplicate_or_missing_translation", str(path), f"{group}: {lang}")
        expected[group][lang] = url
        if url not in pages:
            report("error", "missing_translation", url, f"{group}: {lang}")
    groups = {url: family for family in expected.values() for url in family.values()}
    sitemap = [child.text for child in ElementTree.parse(root / "sitemap.xml").iter() if child.tag.endswith("}loc")]
    if len(sitemap) != len(set(sitemap)):
        report("error", "duplicate_sitemap", "/sitemap.xml", "Há URLs duplicadas")
    sitemap = set(sitemap)
    for item in sitemap:
        path = urlsplit(item).path
        if not item.startswith(base + "/") or (path not in pages and not (root / path.lstrip("/")).is_file()):
            report("error", "bad_sitemap_entry", item, "URL ausente ou fora do domínio")

    titles, descriptions, graph = defaultdict(list), defaultdict(list), defaultdict(set)
    for url, page in sorted(pages.items()):
        label = base + url
        is_error = url == "/404.html"
        for group, label_value in ((titles, page.title), (descriptions, page.meta.get("description", ""))):
            group[label_value.strip()].append(url)
        if not page.title.strip():
            report("error", "title", url, "Título ausente")
        if not page.meta.get("description"):
            report("warning", "description", url, "Descrição ausente")
        if not page.lang:
            report("error", "lang", url, "Idioma ausente")
        if page.canonicals != [label]:
            report("error", "canonical", url, str(page.canonicals))
        if url != "/c.html" and page.meta.get("og:locale") != locales.get(page.lang, {}).get("locale"):
            report("error", "og_locale", url, str(page.meta.get("og:locale")))
        directives = {word for name in ("robots", "googlebot", "bingbot")
                      for word in re.findall(r"[a-z]+", page.meta.get(name, "").lower())}
        if is_error and (label in sitemap or "noindex" not in directives):
            report("error", "404_indexing", url, "A 404 deve ficar fora do sitemap e ter noindex")
        elif not is_error and (label not in sitemap or directives & {"noindex", "nofollow"}):
            report("error", "indexing", url, "Fora do sitemap ou com diretiva restritiva")
        headings = page.headings
        if headings.count(1) != 1 or any(b > a + 1 for a, b in zip(headings, headings[1:])):
            report("warning", "headings", url, str(headings))

        alternatives = dict(page.alternates)
        if len(alternatives) != len(page.alternates):
            report("error", "duplicate_hreflang", url, str(page.alternates))
        if url in groups:
            family = {language: base + target for language, target in groups[url].items()}
            if "pt-BR" in family:
                family["x-default"] = family["pt-BR"]
            if family != alternatives:
                report("error", "translation_group", url, str(alternatives))
        for lang, address in page.alternates:
            target = pages.get(urlsplit(address).path)
            if not target or not address.startswith(base + "/"):
                report("error", "hreflang_target", url, address)
            elif lang != "x-default" and target.lang != lang:
                report("error", "hreflang_lang", url, address)
            elif dict(target.alternates).get(page.lang) != label:
                report("error", "hreflang_reciprocity", url, address)

        person = base + "/autor/#pessoa"
        if url != "/c.html" and len(page.graphs) != 1:
            report("error", "jsonld_count", url, str(len(page.graphs)))
        for raw in page.graphs:
            try:
                nodes = json.loads(raw)["@graph"]
                assert isinstance(nodes, list) and all(isinstance(node, dict) for node in nodes)
            except (ValueError, KeyError, TypeError, AssertionError):
                report("error", "jsonld", url, "Grafo JSON-LD inválido")
                continue
            if [n.get("@id") for n in nodes if n.get("@type") == "Person"] != [person]:
                report("error", "person", url, "Identidade do autor divergente")
            for node in nodes:
                if node.get("@type") in {"BlogPosting", "Book"} and node.get("author") != {"@id": person}:
                    report("error", "author", url, str(node.get("author")))
                if node.get("@type") == "BlogPosting" and (node.get("inLanguage") != page.lang or node.get("url") != label):
                    report("error", "article_identity", url, "Idioma ou URL divergente")

        for tag, address, line in page.links:
            target = urlsplit(urljoin(label, address))
            if target.scheme not in {"http", "https"} or target.netloc != urlsplit(base).netloc:
                continue
            path = trim_index(unquote(target.path))
            if path not in pages and path + "/" in pages:
                path += "/"
            if path in pages:
                fragment = unquote(target.fragment)
                if fragment and not fragment.startswith(":~:") and fragment not in pages[path].ids:
                    report("error", "broken_fragment", url, address, line)
                if tag == "a":
                    graph[url].add(path)
            elif not (root / path.lstrip("/")).is_file():
                report("error", "broken_link", url, address, line)
    for values, name in ((titles, "duplicate_title"), (descriptions, "duplicate_description")):
        for key, urls in values.items():
            if key and len(urls) > 1:
                report("warning", name, urls[0], ", ".join(urls))
    visited = {"/"}
    pending = deque(visited)
    while pending:
        new = graph[pending.popleft()] - visited
        visited.update(new)
        pending.extend(new)
    for url in sorted(set(pages) - visited - {"/404.html"}):
        report("warning", "orphan", url, "Sem caminho de navegação a partir da home")
    return len(pages), findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--source", type=Path, default=Path("."))
    parser.add_argument("--base", default="https://oocomjava.com.br")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    pages, results = audit(args.build, args.source, args.base.rstrip("/"))
    for item in results:
        where = item["url"] + (f":{item['line']}" if item["line"] else "")
        print(f"{item['severity'].upper()} {item['rule']} {where} — {item['detail']}")
    counts = Counter(item["severity"] for item in results)
    print(f"{pages} páginas · {counts['error']} erros · {counts['warning']} avisos")
    if args.json:
        args.json.write_text(json.dumps({"pages": pages, "issues": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return int(counts["error"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
