---
layout: post
title: "JDK, JRE, JVM의 차이: Java에서 각각 무엇인가?"
date: 2026-11-25
lang: ko
translation_id: jdk-jre-jvm-diferencas
permalink: /ko/jdk-jre-jvm-differences/
share_text: >-
  JVM, JRE, JDK의 역할과 Java 환경을 확인하는 명령어를 알아봅니다.
---

## JVM, JRE, JDK
**JVM**(Java Virtual Machine)은 Java 바이트코드를 실행합니다. 클래스를 로드하고 명령을 검증 및 실행하며 메모리 같은 자원을 관리합니다. 호환되는 JVM이 있으면 같은 바이트코드를 여러 시스템에서 실행할 수 있습니다.

**JRE**(Java Runtime Environment)는 JVM과 라이브러리를 포함해 Java 애플리케이션을 실행하는 환경을 뜻합니다. 독립형 JRE 패키지 제공 여부는 배포판과 버전에 따라 다릅니다. 일부 애플리케이션은 자체 런타임을 포함합니다.

**JDK**(Java Development Kit)는 런타임 환경과 개발 도구를 함께 제공합니다. 컴파일러 <code>javac</code>, 실행 도구 <code>java</code>, 애플리케이션을 만들고 실행하고 진단하는 도구가 포함됩니다.

## 프로그래밍하려면 무엇을 설치해야 할까?
Java 개발에는 프로젝트에 맞는 JDK를 설치합니다. 선택한 배포판이 JVM과 필요한 도구를 제공합니다. Oracle JDK와 Eclipse Temurin이 배포판의 예입니다.

터미널에서 다음 명령을 확인합니다.

~~~text
java --version
javac --version
~~~

첫 번째는 Java 실행 도구의 버전을, 두 번째는 컴파일러 버전을 보여 줍니다. <code>java</code>는 작동하지만 <code>javac</code>를 찾을 수 없다면 JDK 설치와 JDK의 <code>bin</code> 디렉터리가 <code>PATH</code>에 있는지 확인하세요.

Windows에서는 <code>where java</code>, <code>where javac</code>를, macOS와 Linux에서는 <code>which java</code>, <code>which javac</code>를 사용해 현재 실행 파일을 확인할 수 있습니다.

## 소스 코드에서 실행까지
<code>Hello.java</code> 파일을 컴파일하고 실행합니다.

~~~text
javac Hello.java
java Hello
~~~

첫 명령은 <code>Hello.class</code>를 생성하고 두 번째 명령은 JVM을 시작해 클래스를 실행합니다. 호환성은 컴파일과 실행에 사용한 버전 모두에 따라 달라집니다.

## 참고 자료
- [Java 플랫폼과 JVM 개요](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [JDK 설치 안내서](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
