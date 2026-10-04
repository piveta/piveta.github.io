---
layout: post
title: "Java 中的异常类"
date: 2026-08-27
lang: zh
translation_id: classes-de-excecao
permalink: /java-exception-classes-zh/
image: /images/descendentesThrowable.png
share_text: >-
  Java异常层次以Throwable为基础，包含Error和Exception等分支，而RuntimeException属于非受检异常。本文说明受检异常与非受检异常的区别。
---
在程序执行过程中，可能会出现需要特殊处理的情况。这些情况可能表示异常或错误条件、程序员未预料到的情况，甚至可能表示另一种执行流程。这些情况称为**异常**。

在 Java 中，异常由属于 `Throwable` 类或其某个子类的对象表示。理解异常层次结构对于了解程序可以抛出、捕获和处理哪些异常非常重要。

## Throwable

`Throwable` 是 Java 异常层次结构的基类。该类的对象保存有关某个特定事件的信息，并允许将这些信息从异常发生的位置传递到负责处理异常的代码。

只有属于 `Throwable` 或其某个子类的对象，才能由 JVM 或程序员使用 `throw` 抛出。同样，`catch` 子句也只能捕获属于该层次结构的对象。

`Throwable` 的主要方法包括 `getMessage()`，它用于获取与异常关联的消息，以及 `printStackTrace()`，它用于显示直到异常发生位置的执行堆栈跟踪。

`Throwable` 类有两个直接子类：`Exception` 和 `Error`。

<img src="/images/descendentesThrowable.png"
     alt="Throwable 层次结构"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

`Error` 类表示应用程序通常无法恢复的严重条件。这些是程序执行过程中通常不应该发生的异常情况。

`Error` 的一些重要子类包括 `AssertionError`、`IOError` 和 `VirtualMachineError`。后者还包括 `InternalError`、`OutOfMemoryError`、`StackOverflowError` 和 `UnknownError` 等子类。

错误可以由 JVM 本身抛出，通常是操作系统或运行环境检测到某些条件的结果。程序员也可以显式地产生错误，例如使用 `assert` 或 `throw`。

<img src="/images/exceptionsError.png"
     alt="Error 及其子类"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

`Exception` 类表示在某些情况下可以处理、并且应用程序可以从中恢复的异常。

它的子类包括 `IOException`、`SQLException`、`ReflectiveOperationException`、`ClassNotFoundException` 和 `RuntimeException`。

不是 `RuntimeException` 子类的 `Exception` 子类称为**受检异常**（*checked exceptions*）。编译器要求程序显式地处理这些异常。可以通过使用 `catch` 子句捕获异常，或者使用 `throws` 声明方法可能抛出该异常来实现。

<img src="/images/descendentesException.png"
     alt="Exception 及其子类"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

在 `Exception` 的子类中，`RuntimeException` 尤为重要。它及其子类称为**运行时异常**（*runtime exceptions*）。

`RuntimeException` 及其子类属于**非受检异常**（*unchecked exceptions*）。编译器不要求使用 `try`/`catch` 显式处理它们，也不要求使用 `throws` 声明它们。

这种异常通常表示逻辑错误或程序使用不当。常见示例包括：

- `ClassCastException`：无法进行显式类型转换时发生。
- `IllegalArgumentException`：表示方法接收到被认为无效或不适当的参数。
- `IndexOutOfBoundsException`：尝试访问索引结构中不存在的位置时发生。
- `NullPointerException`：对 `null` 引用执行操作时发生。

可能抛出 `RuntimeException` 的方法不需要使用 `throws` 声明这种可能性。当然，也可以使用 `try` 和 `catch` 捕获并处理这些异常。

实际上，许多 `RuntimeException` 实例表示本来可以由程序自身避免的问题。当这种异常发生时，通常应该调查其原因并修复问题，而不是简单地捕获异常。

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException 及其子类"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## 受检异常和非受检异常

Java 异常层次结构中的一个重要区别是**受检异常**和**非受检异常**。

`Throwable` 及其所有不是 `RuntimeException` 或 `Error` 子类的子类称为**受检异常**。`RuntimeException` 及其子类，以及 `Error` 及其子类，称为**非受检异常**。

受检异常必须由程序处理或显式声明。这意味着，当一个方法可能抛出受检异常时，必须通过 `catch` 子句处理该异常，或者在方法的 `throws` 子句中声明它。

另一方面，非受检异常不需要显式处理或声明。编译器不要求捕获或声明 `RuntimeException`、`Error` 或它们的子类。

简化后，该层次结构可以表示如下：

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

这种组织方式允许在层次结构的不同级别进行处理。例如，根据所需的行为，`catch` 子句可以捕获某个具体异常，也可以捕获它的某个超类。

理解这一层次结构是理解 Java 异常处理机制的基础，也是决定哪些异常应该处理、哪些应该传播，以及哪些表示需要在程序本身中修复的错误的基础。

本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> 一书的内容，作者为 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>。
