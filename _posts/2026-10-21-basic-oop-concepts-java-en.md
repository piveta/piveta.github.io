---
layout: post
title: "Basic Object-Oriented Programming Concepts"
date: 2026-10-21
lang: en
translation_id: conceitos-basicos-poo-java
permalink: /en/basic-oop-concepts/
share_text: >-
  An introduction to object-oriented programming: classes, objects, attributes, methods, encapsulation, inheritance, polymorphism, and relationships between classes.
---

Structured programming provides mechanisms for modularizing the concepts involved in a software system by defining data structures and the algorithms that manipulate them. Commonly used structured languages make it possible to represent different data types and variables to express the characteristics and properties of the concepts involved, as well as procedures and functions to model the operations associated with them.

However, when we try to reuse components written in structured languages, we must identify the relationships between data (represented by data structures, data types, and variables) and behavior (expressed through procedures and functions). As a result, reuse usually happens at a fine-grained level and often requires considerable effort—for example, to determine which procedures and functions are related to which data structures. Although reusable libraries can be defined, the relationship between data and behavior is not explicit or localized in a single abstraction.

**Object-oriented programming** (OOP) is a programming paradigm that represents the concepts of a particular application domain through abstract data types called classes. These classes model both the characteristics and properties of those concepts and the operations associated with them. OOP extends structured programming by providing ways to specify classes and compose them to model complete computational systems, aiming for greater modularity and component reuse than programs written in structured languages.

Today, object-oriented programming is one of the most widely accepted and used paradigms for software development. Many modern languages support it, including Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift, and Ruby.

A **class** is an abstraction mechanism used to represent concepts from a particular application domain. In a banking domain, for example, the concepts might include branches, accounts, customers, and transactions. We could therefore define classes such as `Branch`, `Account`, `Customer`, and `Transaction` to represent them. The figure shows a graphical representation of these classes.

<img src="/images/en/oopClasses.svg" alt="Classes Branch, Account, Customer, and Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Classes serve as *templates* for creating concrete, manipulable examples of these concepts. Such examples are called **objects**. An object is said to be an **instance** of a class, and the process of creating objects is called **instantiation**. For example, we could create objects to represent customers *John*, *Peter*, and *Mary*, together with their personal information and the functionality available to customers.

<img src="/images/en/oopObjects.svg" alt="Objects John, Peter, and Mary, each an instance of the Customer class." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

A class is defined to represent the properties, characteristics, and behavior of a concept. The two main mechanisms for doing so are attributes and methods.

**Attributes** represent characteristics or properties of objects in a class. Examples of attributes of a `Customer` class include *name*, *age*, *address*, and *marital status*. When instantiated, each particular customer can have different values for these attributes. For instance, an object representing a customer might have the following values: *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street, and *marital status* $`=`$ married.

**Methods** represent behavior. Possible methods of an `Account` class might be related to the operations of *opening*, *closing*, or *changing the account holder*. **Invoking** a method (also called **calling** a method) causes the operation implemented by that method to execute. Classes commonly have special methods for creating (instantiating) objects, called **constructors**, and for destroying objects, called **destructors**.

Attributes and methods also fall into two categories: instance and class. **Instance attributes and methods** are the most commonly used and are accessed through objects of the class. They represent characteristics and operations associated with individual instances. Examples of instance attributes of an `Account` class include *bank*, *branch*, *account number*, and *account holder*. Instance methods are operations on a specific account, such as *withdraw*, *transfer*, and *deposit*. **Class attributes and methods**, on the other hand, belong to the class itself rather than to its instances. For example, a class attribute could count how many `Account` instances have been created, and a class method could retrieve that count.

To restrict access to attributes and methods, classes provide mechanisms for **encapsulation and information hiding**. Programming languages commonly support visibility modifiers that specify who can access a particular attribute, method, or class.

Classes are abstraction mechanisms in which concepts from the real and computational worlds are represented and encapsulated in a class structure. These abstractions can be combined through composition mechanisms (relationships) so that classes work together to meet an application's requirements. The main relationships between classes include inheritance, association, aggregation, composition, and realization.

**Inheritance** is a composition mechanism that lets classes reuse the interface and behavior of existing classes by extending their functionality. A class that extends another through inheritance is called a **subclass** of the other class, while the extended class is called its **superclass**. The extension is usually specified in the subclass (for example, `SubClass` extends `SuperClass`).

Figure 3 shows the classes `Shape`, `Rectangle`, `Triangle`, and `Circle`. In this figure, `Shape` is the superclass, and `Rectangle`, `Triangle`, and `Circle` are its subclasses.

<img src="/images/en/oopInheritance.png" alt="The Shape class is the superclass of Rectangle, Triangle, and Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Inheritance mechanisms vary across programming languages. These variations usually concern inheritance visibility and multiplicity. Some languages, such as C++, allow **inheritance visibility** to be specified as **public** or **private**. Consider a class `A` and a class `B` that inherits from (or extends) `A`. Then `A` is a superclass of `B`, and `B` is a subclass of `A`. With public inheritance, if `B` inherits from `A`, then `B` is an `A` (that is, `B` is a subtype of `A`), and `B` inherits both the implementation and the interface of `A`. Wherever an object of class `A` is required, an object of class `B` (or any other subclass of `A`) can be used, because every instance of `B` is also considered an instance of `A`. This principle is called the **Liskov substitution principle**. With private inheritance, `B` is not an `A`; only `A`'s implementation is inherited. In this case, `B` is implemented in terms of `A`, and the Liskov substitution principle does not apply.

Inheritance can also be **single or multiple**, depending on the multiplicity of the relationship. With single inheritance, used by languages such as Java and C#, a class can have only one superclass. With multiple inheritance, used by C++, for example, a class can have more than one superclass. Language designers do not agree on whether the benefits of multiple inheritance justify the problems associated with its use. Other languages offer alternatives, such as virtual inheritance (based on interfaces), *traits*, and *mixins*.

Figure 4 shows an example of multiple inheritance. Here, `Mammal` and `Bird` represent animals, and each has subclasses: `Horse`, `Dog`, and `Bat` are subclasses of `Mammal`, while `Ostrich` and `Duck` are subclasses of `Bird`. We also want to classify animals that can fly. To do so, we create a `Flyer` class, which represents flying objects that are not necessarily animals. With multiple inheritance, we can say that objects of both `Duck` and `Bat` are also flying objects (they inherit from `Flyer`).

<img src="/images/en/oopMultipleInheritance.png" alt="Multiple inheritance among Animal, Bird, Flyer, and Mammal classes." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Some classes are **abstract**. Like other classes (called **concrete**), they represent the characteristics and behavior of a set of real-world objects. However, abstract classes cannot be instantiated directly. For example, in the multiple-inheritance diagram, `Mammal`, `Bird`, and `Flyer` could be abstract classes because there are no direct examples of these classes in the real world—only examples of their subclasses, such as horses, dogs, and ducks.

Besides visibility and multiplicity, inheritance also enables polymorphic methods. In object-oriented programming, **polymorphism** is the ability of an operation to behave differently depending on the class of the object that calls it. The main forms of polymorphism are:

- **Ad hoc polymorphism (or overloading)**, which occurs when a class has methods with the same name but different formal parameter types. A call can invoke a particular method depending on the actual argument used;

- **Parametric polymorphism**, which occurs when a method is defined generically and is associated with a type that is specified later (for example, when a variable is declared or an object is instantiated). In object-oriented languages, such types are called generic types;

- **Subtype polymorphism**, which occurs when subclasses override methods from one of their superclasses. The object making the call determines which method is executed. This is normally resolved at runtime through late binding.

Besides inheritance, other relationships include association, aggregation, and composition. In general, these relationships differ in the degree of coupling between their participants:

- In an **association**, the relationship between objects is usually temporary and can be changed easily at runtime. In a traffic-related domain, for example, a person can be associated with a particular vehicle in the role of driver. This association can be changed whenever the vehicle's driver changes. Both objects continue to exist even if the association is removed.

- In an **aggregation**, the relationship is stronger than an association. The aggregated objects are commonly created when the aggregating object is created. Using the same domain as the previous example, a car could have four wheels: the car is the aggregating object, and the wheels are the aggregated objects. Although the relationship between the wheels and the car can be removed, it is stronger than an association (changing a car's wheels is less common and more involved than changing its driver).

- In a **composition**, the relationship is stronger still. It differs from the other relationships because the composed objects are parts of a larger object. For example, the fabric of a vehicle's seat is made of threads. If the threads cease to exist, the seat also ceases to exist (or at least loses its identity).

These relationships between objects are often conceptual. When mapping them to a programming language, for example, we associate, aggregate, and compose objects through class attributes (setting the values of those attributes in objects at runtime, for instance). What sometimes changes is when the objects are created. In a composition, the composed objects are commonly created in the constructor of the whole; in an association, the associated objects are usually created independently in different parts of the code and linked when needed.

One final relationship, **realization**, occurs when a class declares that it implements an interface. An **interface** can be viewed as an abstract class whose methods are all abstract[^1]. It serves as a protocol between clients and implementers of the interface. In this case, the class (or one of its subclasses) must implement the methods described by the interface. Clients can therefore write code that conforms to the interface without needing to know how the implementing classes do so.

[^1]: In Java, for example, since version 8, interfaces can define concrete methods called default methods (using the `default` keyword). Classes that implement an interface with a default method do not have to provide an implementation for that method, although they may do so if they wish.

---

*This article is adapted from content in <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, a book by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Related articles

- [The original article in Portuguese: Conceitos Básicos de Orientação a Objetos](/conceitos-basicos-poo-java/)
- [Classes in Java](/classes-em-java/) (Portuguese)
- [Inheritance in Java](/heranca-em-java/) (Portuguese)
- [Polymorphism in Java](/polimorfismo-em-java/) (Portuguese)
- [Interfaces in Java](/interfaces-em-java/) (Portuguese)
- [OOP and Java links](/links-poo-java/) (Portuguese)
- [Object-Oriented Programming Exercises](/exercicios-poo-java/) (Portuguese)
