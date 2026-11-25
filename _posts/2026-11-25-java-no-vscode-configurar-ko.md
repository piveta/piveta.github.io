---
layout: post
title: "VS Code에서 Java 설정하기: JDK 설치와 구성"
date: 2026-11-25
lang: ko
translation_id: java-no-vscode-configurar
permalink: /ko/java-vscode-setup/
share_text: >-
  Visual Studio Code에서 Java를 설정하고 JDK를 선택해 첫 프로그램을 실행합니다.
---

## JDK와 Visual Studio Code 설치
**VS Code에서 Java**를 개발하려면 프로젝트와 호환되는 JDK와 Visual Studio Code를 설치합니다. 터미널에서 JDK를 확인합니다.

~~~text
java --version
javac --version
~~~

명령을 찾지 못하면 JDK 설치와 <code>PATH</code>를 확인하세요. 환경 변수를 바꾼 뒤에는 새 터미널을 엽니다.

## Java 확장 설치
VS Code에서 **Extensions**를 열고 **Extension Pack for Java**를 검색해 Microsoft가 배포한 패키지를 설치합니다. 언어 지원, 실행, 디버깅 등 Java 도구가 포함되어 있습니다.

Windows와 macOS에서는 VS Code, JDK, 필수 확장을 묶은 Coding Pack for Java도 사용할 수 있습니다.

## 프로젝트 JDK 구성
Windows와 Linux에서는 <code>Ctrl+Shift+P</code>, macOS에서는 <code>Cmd+Shift+P</code>로 명령 팔레트를 엽니다. **Java: Configure Java Runtime**을 실행해 프로젝트에 연결된 JDK를 확인합니다.

프로젝트가 선택한 JDK와 터미널의 JDK가 다를 수 있습니다. 여러 버전이 설치되어 있다면 둘 다 확인하세요.

## 프로그램 실행
VS Code에서 폴더를 열고 <code>Hello.java</code>를 만듭니다.

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Java 25부터 제공되는 간결한 소스 파일 문법과 <code>IO.println</code>을 사용합니다. <code>main</code> 옆의 **Run**을 선택하고 터미널 출력을 확인합니다. 디버깅하려면 **Debug**를 선택하고 중단점을 설정합니다.

파일이 인식되지 않으면 폴더가 열려 있는지, 확장 기능이 시작되었는지, **Java: Configure Java Runtime**의 JDK 설정이 맞는지 확인하세요.

## 참고 자료
- [VS Code에서 Java 시작하기](https://code.visualstudio.com/docs/java/java-tutorial)
- [VS Code의 Java 프로젝트 관리](https://code.visualstudio.com/docs/java/java-project)
