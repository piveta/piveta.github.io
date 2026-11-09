---
layout: post
title: "面向对象编程练习"
date: 2026-10-21
lang: zh
translation_id: exercicios-poo-java
permalink: /oop-exercises-zh/
share_text: >-
  关于 OOP 概念、多态、继承、抽象类、泛型、Java 和银行账户的练习。
---

1. 编写一篇教程，说明如何在 Java 以外的任意语言中表示面向对象编程的基本概念。

2. 描述多态、它的产生方式以及对系统编程的影响，包括优缺点。请举例说明。

3. 定义面向对象编程语言中的方法重写（*overriding*）和方法重载（*overloading*），并举例说明。

4. 定义继承，并描述三种适合使用继承的情况。请附上代码示例。

5. 什么是抽象类？它们在面向对象编程语言中有什么用途？请描述至少三种适合使用抽象类的情况。

6. 泛型类型在面向对象系统中有哪些优点，应该在何时使用？请至少举出三种适用情况。

7. 请考虑以下关于面向对象编程的陈述：

   I. 方法定义类中的操作。

   II. 类是用于表示现实世界和计算机世界概念的抽象。

   III. 类实例通常由构造器创建，构造器会创建特定类的对象。

   请选择正确选项：

   1. 只有陈述 I 不正确。
   2. 只有陈述 II 不正确。
   3. 只有陈述 III 不正确。
   4. 只有陈述 I 和 III 不正确。
   5. 所有陈述都正确。

8. 请选择关于 Java 继承的正确陈述：

   1. 超类对象总能赋值给其某个子类类型的变量，且不会发生编译错误。
   2. 继承是从类外部访问方法和字段的唯一方式。
   3. 超类方法的行为无法被完全替换，只能扩展。
   4. 重载是在超类中定义多个参数相同的方法，以供其子类使用。
   5. 子类继承超类的所有非私有字段和方法，并可以添加新的字段和方法。

9. 创建用于管理银行账户的类。账户可以是储蓄账户或支票账户。需要支持以下操作：

   - 获取账户余额。
   - 修改账户余额。
   - 从账户取款。
   - 向账户存款。
   - 向其他账户转账。
   - 冻结和解冻账户，例如 `account1.block()` 和 `account1.unblock()`。账户被冻结时，只能读取或修改余额。

10. 使用 Java 实现一个可在终端运行的*扫雷*游戏。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a> 所著《<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>》中的内容。*

## 相关文章

- [面向对象编程的基本概念](/oop-basics-java-zh/)
- [Java 中的类](/classes-in-java-zh/)
- [Java 中的继承](/inheritance-in-java-zh/)
- [Java 中的多态](/polymorphism-in-java-zh/)
- [Java 中的接口](/interfaces-in-java-zh/)
- [OOP 与 Java 链接](/oop-java-links-zh/)
