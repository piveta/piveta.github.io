---
layout: post
title: "Windows에 Java와 JDK 설치하기"
date: 2026-11-25
lang: ko
translation_id: como-instalar-java-jdk-windows
permalink: /ko/install-java-jdk-windows/
share_text: >-
  Windows에서 JDK를 내려받아 설치하고 java와 javac로 확인하는 방법을 알아봅니다.
---

## Java 배포판 선택
Windows에서 Java를 개발하려면 프로젝트와 호환되는 **JDK**를 내려받습니다. Oracle JDK와 Eclipse Temurin이 있습니다. 장기 지원이 필요한 프로젝트에는 LTS 버전이 적합할 수 있습니다. 프로젝트 요구 사항과 배포판 이용 조건을 확인하세요.

Windows 설정에서 시스템 종류와 프로세서 아키텍처를 확인하고, x64 또는 AArch64 등 맞는 패키지와 Windows 설치 프로그램을 선택합니다.

## JDK 다운로드 및 설치
Eclipse Temurin 설치 방법:

1. [Adoptium 다운로드 페이지](https://adoptium.net/temurin/releases/)를 엽니다.
2. Java 버전, Windows, 아키텍처, **JDK** 패키지를 선택합니다.
3. MSI 설치 프로그램을 내려받아 실행합니다.
4. Java를 <code>PATH</code>에 추가하는지 확인합니다. 다른 도구가 <code>JAVA_HOME</code>을 요구하면 해당 옵션도 선택합니다.
5. 설치를 마치고 새 터미널을 엽니다.

Temurin에서 <code>PATH</code> 추가는 기본 옵션이며 <code>JAVA_HOME</code> 설정은 추가 옵션입니다.

## 설치 확인
PowerShell 또는 명령 프롬프트에서 실행합니다.

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

앞의 두 명령은 Java와 컴파일러 버전을 출력합니다. 나머지는 <code>PATH</code>에서 찾은 실행 파일을 보여 줍니다. 명령을 찾지 못하면 새 터미널을 열고 환경 변수를 확인하세요. 다른 버전이 나오면 <code>PATH</code>의 디렉터리 순서를 살펴봅니다.

컴파일을 시험하려면 다음 코드를 <code>Hello.java</code>로 저장합니다.

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Java 25부터 가능한 간결한 소스 파일 문법과 <code>IO.println</code>을 사용합니다. 실행 명령:

~~~text
javac Hello.java
java Hello
~~~

출력은 <code>Hello World!</code>입니다. Java 25 이전에는 설치된 JDK가 지원하는 형식을 사용하세요.

## 참고 자료
- [Eclipse Temurin MSI 설치 프로그램](https://adoptium.net/installation/windows/)
- [Oracle JDK 설치 안내](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
