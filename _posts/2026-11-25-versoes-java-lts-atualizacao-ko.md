---
layout: post
title: "Java 버전: LTS, 업데이트, 버전 확인 방법"
date: 2026-11-25
lang: ko
translation_id: versoes-java-lts-atualizacao
permalink: /ko/java-versions-lts-updates/
share_text: >-
  Java 릴리스 주기와 LTS의 의미, JDK 버전 확인 및 업데이트 방법을 알아봅니다.
---

## Java 버전 확인
터미널에서 다음 명령을 실행합니다.

~~~text
java --version
javac --version
~~~

첫 번째는 애플리케이션을 실행하는 Java 실행 도구의 버전을, 두 번째는 컴파일러 버전을 확인합니다. JDK가 여러 개 설치되어 있으면 <code>PATH</code>에서 찾은 실행 파일이 IDE에 설정된 것과 다를 수 있습니다.

## Java 버전과 LTS
Java는 6개월마다 기능 릴리스를 제공합니다. **LTS**(장기 지원) 버전은 일부 공급업체에서 장기 지원을 받습니다. 지원 기간, 가격, 조건은 배포판과 공급업체마다 다릅니다.

Oracle 지원 로드맵에서 Java 8, 11, 17, 21, 25는 LTS 버전입니다. Oracle은 2년마다 새 LTS를 계획합니다. 운영 환경 버전을 선택하기 전에 최신 로드맵과 공급업체 정책을 확인하세요.

선택은 라이브러리, 도구, 애플리케이션 요구 사항에도 달려 있습니다. LTS는 더 긴 지원 기간을 제공하며 중간 버전은 새 기능을 일찍 제공합니다.

## 버전 및 JEP 확인
Oracle의 [JDK 릴리스 노트 색인](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html)에는 각 릴리스와 업데이트 링크가 있습니다. 릴리스 노트에서 변경 사항, 수정 사항, 추가되거나 제거된 기능을 확인할 수 있습니다. [JDK 27 릴리스 노트](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html)는 새 기능과 관련 JEP를 설명합니다.

**JEP**(JDK Enhancement Proposal)는 JDK 개선 제안의 목표, 설계, 상태를 기록합니다. 기능은 먼저 *preview* 또는 *incubator*로 제공되어 정식 기능이 되기 전에 바뀔 수 있습니다.

[릴리스별 Java 언어 변경 사항](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html)과 [언어 변경 요약](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html)에서 정식 및 미리보기 기능을 비교할 수 있습니다.

## Java 업데이트
1. <code>java --version</code>과 <code>javac --version</code>으로 현재 버전을 확인합니다.
2. 프로젝트, 의존성, 운영 환경의 지원 버전을 확인합니다.
3. 현재 배포판의 업데이트를 받거나 호환되는 배포판을 선택합니다.
4. JDK를 설치하고 필요하면 <code>PATH</code>, <code>JAVA_HOME</code>, IDE를 조정합니다.
5. 새 터미널에서 버전을 확인하고 애플리케이션 테스트를 실행합니다.

같은 버전 계열의 업데이트와 주요 버전 마이그레이션은 서로 다른 결정입니다. 마이그레이션 전에 릴리스 노트를 살펴보고 애플리케이션과 의존성을 테스트하세요.

Windows에서는 <code>where.exe java</code>와 <code>where.exe javac</code>, macOS와 Linux에서는 <code>which java</code>와 <code>which javac</code>를 사용합니다.

## 참고 자료
- [Oracle Java SE 지원 로드맵](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Oracle JDK 라이선스 FAQ](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
