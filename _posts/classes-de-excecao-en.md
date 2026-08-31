---
layout: post
title: "Exception Classes in Java"
date: 2026-08-27
lang: en
translation_id: 2026-08-27-classes-de-excecao
permalink: /exception-classes/ 
---
During program execution, situations may arise that require special handling. They may represent abnormal or erroneous conditions, situations that were not anticipated by the programmer, or even alternative execution flows. These conditions are called **exceptions**.

In Java, exceptions are represented by objects belonging to the `Throwable` class or one of its subclasses. The exception hierarchy is important for understanding which exceptions can be thrown, caught, and handled by programs.

## Throwable

`Throwable` is the base class of the exception hierarchy in Java. Objects of this class store information about a particular occurrence and allow this information to be transferred from the point where the exception occurred to the code responsible for handling it.

Only objects belonging to `Throwable` or one of its subclasses can be thrown by the JVM or by the programmer using `throw`. Likewise, a `catch` clause can only catch objects belonging to this hierarchy.

Among the main methods of `Throwable` are `getMessage()`, which allows the message associated with the exception to be obtained, and `printStackTrace()`, which displays the execution stack trace up to the point where the exception occurred.

The `Throwable` class has two direct subclasses: `Exception` and `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Throwable hierarchy"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

The `Error` class represents serious conditions from which an application generally cannot recover. These are abnormal situations that normally should not occur during program execution.

Some important subclasses of `Error` are `AssertionError`, `IOError`, and `VirtualMachineError`. The latter has, among others, subclasses such as `InternalError`, `OutOfMemoryError`, `StackOverflowError`, and `UnknownError`.

Errors can be thrown by the JVM itself, often as a consequence of conditions detected by the operating system or the runtime environment. They can also be explicitly produced by the programmer, for example, through `assert` or `throw`.

<img src="/images/exceptionsError.png"
     alt="Error and its subclasses"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

The `Exception` class represents exceptions that, under certain circumstances, can be handled and from which the application can recover.

Its subclasses include `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException`, and `RuntimeException`.

The `Exception` subclasses that are not subclasses of `RuntimeException` are called **checked exceptions**. The compiler requires them to be explicitly accounted for by the program. This can be done by catching the exception with a `catch` clause or by declaring, using `throws`, that the method may throw it.

<img src="/images/descendentesException.png"
     alt="Exception and its subclasses"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Among the subclasses of `Exception`, `RuntimeException` stands out. It and its subclasses are called **runtime exceptions**.

`RuntimeException` and its subclasses are **unchecked exceptions**. The compiler does not require them to be explicitly handled with `try`/`catch` or declared with `throws`.

This type of exception usually represents logical errors or incorrect use of a program. Common examples include:

- `ClassCastException`: occurs when an explicit type conversion is not possible.
- `IllegalArgumentException`: indicates that a method received an argument considered invalid or inappropriate.
- `IndexOutOfBoundsException`: occurs when an attempt is made to access a nonexistent position in an indexed structure.
- `NullPointerException`: occurs when an operation is performed on a `null` reference.

A method that may throw a `RuntimeException` does not need to declare this possibility with `throws`. Naturally, it is still possible to catch and handle these exceptions with `try` and `catch`.

In practice, many `RuntimeException` instances indicate problems that could have been prevented by the program itself. When one occurs, it is usually important to investigate its cause and fix the problem rather than simply catch the exception.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException and its subclasses"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">
     
## Checked and unchecked exceptions

An important distinction in Java's exception hierarchy is between **checked** and **unchecked** exceptions.

`Throwable` and all of its subclasses that are not subclasses of `RuntimeException` or `Error` are called **checked exceptions**. `RuntimeException` and its subclasses, as well as `Error` and its subclasses, are called **unchecked exceptions**.

Checked exceptions must be handled or explicitly declared by the program. This means that when a method can throw a checked exception, it must be handled by a `catch` clause or declared in the method's `throws` clause.

Unchecked exceptions, on the other hand, do not need to be explicitly handled or declared. The compiler does not require `RuntimeException`, `Error`, or their subclasses to be caught or declared.

In simplified form, the hierarchy can be visualized as follows:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```
This organization allows handling to be performed at different levels of the hierarchy. A `catch` clause can, for example, catch a specific exception or one of its superclasses, depending on the desired behavior.

Understanding this hierarchy is fundamental to understanding Java's exception-handling mechanism and to deciding which exceptions should be handled, which should be propagated, and which represent errors that need to be fixed in the program itself.

This article is adapted from content in the book <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
