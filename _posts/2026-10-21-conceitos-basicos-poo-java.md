---
layout: post
title: "Conceitos Básicos de Orientação a Objetos"
date: 2026-10-21
lang: pt-BR
translation_id: conceitos-basicos-poo-java
permalink: /conceitos-basicos-poo-java/
share_text: >-
  O artigo apresenta os fundamentos da orientação a objetos: classes, objetos, atributos, métodos, encapsulamento, herança, polimorfismo e relacionamentos entre classes.
---

A programação estruturada fornece mecanismos para modularizar os
conceitos envolvidos em um sistema de software através da definição de
estruturas de dados e dos algoritmos que as manipulam. As linguagens
estruturadas mais comumente usadas possibilitam a representação de
diferentes tipos de dados e variáveis de forma a expressar as
características e as propriedades dos conceitos envolvidos, bem como
procedimentos e funções para modelar as operações envolvidas.

No entanto, ao tentarmos reusar os componentes expressos através das
linguagens estruturadas, precisamos descobrir a relação entre os dados
(representados pelas estruturas de dados, tipos de dados e variáveis) e
o comportamento (expresso através de procedimentos e funções). Desta
forma, o reuso normalmente ocorre em uma granularidade fina e muitas
vezes demanda um esforço considerável (para identificar, por exemplo,
quais procedimentos e funções relacionam-se com quais estruturas de
dados). Embora seja possível a definição de bibliotecas reutilizáveis, a
relação entre dados e comportamento não é explícita e localizada em uma
única abstração.

A **programação orientada a objetos** (POO) é um paradigma de
programação que visa representar os conceitos de um determinado domínio
de aplicação através da criação de tipos abstratos de dados, chamados
classes, que modelam tanto as características e as propriedades desses
conceitos quanto suas operações. Ela estende a programação estruturada
fornecendo os meios para que as classes sejam especificadas e compostas
entre si de forma a modelar sistemas computacionais completos, visando
uma melhor modularidade e um maior reuso de componentes que os programas
escritos em linguagens estruturadas.

Atualmente, o paradigma de orientação a objetos é considerado o mais
amplamente aceito e utilizado no desenvolvimento de sistemas de
software. Diversas linguagens modernas fornecem suporte a este
paradigma, incluindo: Java, C++, C#, Python, Kotlin, JavaScript,
TypeScript, Swift e Ruby.



Uma **classe** é um mecanismo de abstração usado para representar
conceitos de um determinado domínio de aplicação. Por exemplo, se
considerarmos um domínio bancário, os conceitos seriam relacionados a
agências, contas, clientes, transações, etc. Desta forma, poderíamos ter
as classes `Agência`, `Conta`, `Cliente`, `Transação`, dentre outras,
para representar os conceitos do domínio. A Figura mostra uma representação gráfica destas classes.

<img src="/images/oopClasses.png" alt="Representação gráfica das classes Agência, Conta, Cliente e Transação." style="max-width: 700px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

As classes servem como *templates* para a criação de exemplares
concretos e manipuláveis desses conceitos. Tais exemplares são chamados
de **objetos**. Diz-se que um objeto é uma **instância** de uma classe.
O processo de criação de objetos é chamado de **instanciação**. Por
exemplo, poderíamos criar objetos para representar os clientes *João*,
*Pedro* e *Maria*, juntamente com suas informações pessoais e as
funcionalidades possíveis para clientes.

<img src="/images/oopObjetos.png" alt="Representação gráfica dos objetos João, Pedro e Maria, instâncias da classe Cliente." style="max-width: 700px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Uma classe é definida de forma a representar as propriedades, as
ca­rac­te­rís­ti­cas e o com­por­ta­men­to de um con­cei­to. Para isso, são usados
prin­ci­pal­men­te dois me­ca­nis­mos: atributos e métodos.

Os **atributos** são utilizados para representar características ou
propriedades dos objetos de uma classe. Exemplos de atributos de uma
classe `Cliente` seriam *nome*, *idade*, *endereço* e *estado civil*.
Dessa forma, ao ser instanciado, cada cliente específico poderia possuir
valores distintos para esses atributos. Por exemplo, um objeto
representando um cliente poderia ter os seguintes valores de atributos:
*nome* $`=`$ João da Silva, *idade* $`=`$ 50, *endereço* $`=`$ Rua
Presidente Vargas, 205, *estado civil* $`=`$ casado.

Os **métodos** são utilizados para representar comportamento. Por
exemplo, possíveis métodos de uma classe `Conta` poderiam estar
relacionados às operações de *abrir*, *encerrar*, ou *alterar o titular*
de uma conta. A **invocação** de um método (também conhecida como
**chamada** a um método) de uma classe faz com que a operação
implementada no método seja executada. Comumente, as classes possuem
métodos especiais para a criação (instanciação) de objetos, chamados de
**construtores** e para a destruição de objetos (**destrutores**).

Os atributos e métodos também dividem-se em duas categorias: de
instância e de classe. Os **atributos e métodos de instância** são os
mais comumente utilizados e são acessados a partir de objetos da classe.
Eles representam características e operações que estão relacionadas com
as instâncias individualmente. Exemplos de atributos de instância de uma
classe `Conta` seriam: *banco*, *agência*, *número da conta*, *titular
da conta*, etc. Métodos de instância seriam operações para uma conta
específica, tais como: *sacar*, *transferir*, *depositar*, etc. Já os
**atributos e métodos de classe** representam atributos e métodos da
classe em si (e não de suas instâncias) como, por exemplo, um atributo
que conta o número de instâncias criadas pela classe `Conta` ou um
método que obtém tal número de instâncias desse atributo.

De forma a restringir o acesso a atributos e métodos, as classes
fornecem mecanismos de **encapsulamento e ocultação de informação**.
Normalmente, o que as linguagens de programação fornecem é o uso de
modificadores de visibilidade, que definem quem consegue enxergar um
determinado atributo, método, ou classe.

As classes servem como mecanismos de abstração, nas quais conceitos do
mundo real e do mundo computacional são representados e encapsulados em
uma estrutura de classe. A partir dessas abstrações, são utilizados
mecanismos de composição (relacionamentos) de forma a unir tais classes
para que elas possam auxiliar a atender aos requisitos da aplicação.
Dentre os diferentes relacionamentos possíveis entre classes,
destacam-se: herança, associação, agregação, composição e realização.

A **herança** é uma mecanismo de composição que permite que as classes
reusem a interface e o comportamento de classes existentes, através da
extensão de suas funcionalidades de maneira aditiva. Normalmente, uma
classe que estende outra classe através de herança é chamada de
**subclasse** da primeira, enquanto a classe estendida é chamada de
**superclasse** da segunda. O usual é que a definição de extensão esteja
especificada na subclasse (algo como: `SubClasse` estende
`SuperClasse`).

Considere, por exemplo, a Figura 3, onde são mostradas
as classes `Figura`, `Retângulo`, `Triângulo` e `Círculo`.

Nessa figura,
a superclasse é a classe `Figura` e as subclasses são `Retângulo`,
`Triângulo` e `Círculo`.

<img src="/images/oopHeranca.png" alt="Exemplo de herança." style="max-width: 700px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

O mecanismo de herança pode variar de acordo com a linguagem de
programação e tais variações normalmente dizem respeito à visibilidade e
à multiplicidade da herança. Algumas linguagens, como C++, permitem que
a **visibilidade da herança** seja especificada como **pública** ou como
**privada**. Considere uma classe `A` e uma classe `B` que herda da (ou
estende a) classe `A`. Diz-se que a classe `A` é uma superclasse de `B`
e que `B` é uma subclasse de `A`. Na herança pública, diz-se que se uma
classe `B` herda de uma classe `A`, então `B` é um `A` (`B` é um subtipo de
`A`), e tanto a implementação quanto a interface de uma classe `A` são
herdadas pela classe `B`. Nesse caso, em todos os lugares em que for
requerido um objeto da classe `A`, pode-se usar um objeto da classe `B`
(ou de qualquer outra subclasse de `A`), dado que qualquer instância de
`B` é considerada também uma instância de `A`. Tal princípio é chamado
de **princípio de substituição de Liskov**. Na herança privada, `B` não é um `A`, apenas a implementação de `A` é herdada. Nesse caso, `B` é implementada em termos de `A`. O
princípio de substituição de Liskov não se aplica em tais casos.

A **herança** pode também ser **simples ou múltipla** em relação à
multiplicidade do relacionamento. Na herança simples, abordagem adotada
por algumas linguagens de programação, tais como Java e C#, uma classe
pode ter apenas uma superclasse. Já no caso da herança múltipla,
abordagem adotada em C++, por exemplo, uma classe pode ter mais de uma
superclasse. Não há um consenso entre os projetistas de linguagens de
programação acerca de se os benefícios proporcionados pela herança
múltipla são suficientes para justificar os problemas relacionados ao
seu uso. Outras linguagens oferecem alternativas, tais como herança
virtual (baseada em interfaces), *traits* e *mixins*.

Considere o exemplo de herança múltipla da Figura 4.
Neste exemplo, temos duas classe que representam animais (`Mamífero` e
`Ave`). Cada uma delas tem algumas subclasses: `Cavalo`, `Cachorro` e
`Morcego` são subclasses de `Mamífero` e `Ema` e `Pato` são subclasses
de `Ave`. No entanto, queremos também classificar os animais que são
voadores. Para isso, criamos uma classe `Voador`, que representa objetos
voadores (não necessariamente animais). Desta forma, usamos o recurso da
herança múltipla para dizer que tanto objetos da classe `Pato` quanto da
classe `Morcego` também são objetos voadores (herdam de `Voador`).

<img src="/images/oopHerancaMultipla.png" alt="Exemplo de herança múltipla." style="max-width: 700px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Algumas classes são ditas **abstratas**. Tais classes representam as
características e o comportamento de um conjunto de objetos do mundo
real da mesma forma que as demais classes (ditas **concretas**). No
entanto, não existem instâncias diretas de tais classes (elas não podem
ser instanciadas). Por exemplo, no caso da herança múltipla, poderíamos
definir as classes `Mamífero`, `Ave` e `Voador` como classes abstratas,
pois não há exemplares diretos dessas classes no mundo real - há apenas
exemplares de suas subclasses (existem apenas cavalos, cachorros, patos,
etc).

Além de questões como a visibilidade e a multiplicidade da herança, seu
uso também possibilita a criação de métodos polimórficos. Em orientação
a objetos, o **polimorfismo** é a capacidade que uma operação tem de ter
um comportamento diferente dependendo da classe do objeto que a chama.
As principais formas de polimorfismo são:

- **Polimorfismo *ad-hoc* (ou de sobrecarga)**, que ocorre quando
  existem métodos de uma classe com mesmo nome, mas com parâmetros
  formais de tipos diferentes. A chamada a um desses métodos pode
  resultar na invocação de um dos métodos específicos dependendo do
  parâmetro real utilizado;

- **Polimorfismo paramétrico**, que ocorre quando um método é criado de
  maneira genérica, vinculado a um tipo que só é definido posteriormente
  (na declaração de uma variável, ou na instanciação de um objeto, por
  exemplo). Em linguagens orientadas a objetos, tais tipos são chamados
  de tipos genéricos;

- **Polimorfismo de subtipo**, que ocorre quando as subclasses
  sobrescrevem métodos de uma de suas superclasses. Nesse caso, a
  determinação de qual método será executado dependerá do objeto que
  está fazendo a chamada. Isso normalmente é realizado em tempo de
  execução, na chamada ligação tardia.

Além do mecanismo de herança, existem outros tipos de relacionamentos,
incluindo os seguintes: associação, agregação e composição. De um modo
geral, o que muda nos diferentes relacionamentos é o grau de acoplamento
entre os participantes:

- Na **associação**, o relacionamento entre objetos comumente é
  transitório e pode ser alterado facilmente em tempo de execução.
  Considerando, por exemplo, objetos que modelam trânsito, podemos ter
  uma pessoa associada a um determinado veículo, no papel de condutora.
  Tal associação pode ser modificada sempre que existir a necessidade de
  alterar o condutor do veículo. Ambos os objetos continuam a existir,
  mesmo que a associação seja desfeita.

- Na **agregação**, o relacionamento é mais forte que na associação.
  Comumente, os objetos agregados são criados no momento da criação do
  objeto agregador. Usando o mesmo domínio do exemplo anterior,
  poderíamos dizer que um carro possui quatro rodas, onde o carro seria
  o objeto agregador e as rodas seriam objetos agregados. Embora a
  associação entre rodas e carro possa ser desfeita, ela é mais forte
  que na associação (é mais incomum e trabalhoso trocarmos rodas de um
  carro que seu condutor).

- Na **composição**, o relacionamento é ainda mais forte que na
  agregação. Esse relacionamento diferencia-se dos demais porque os
  objetos que estão sendo compostos fazem parte de um objeto maior.
  Então, por exemplo, poderíamos dizer que o tecido do banco do assento
  do veículo é composto de fios. Caso os fios deixem de existir, o banco
  também deixará (ou ao menos ficará descaracterizado).

Notem, no entanto, que muitas vezes essa relação entre objetos é algo
conceitual. Ao mapearmos esses relacionamentos para uma linguagem de
programação, por exemplo, associamos, agregamos e compomos objetos
através de atributos de uma classe (configurando o valor de tais
atributos nos objetos em tempo de execução, por exemplo). O que algumas
vezes muda é o momento no qual os objetos são criados. Em uma
composição, por exemplo, os objetos compostos são comumente criados no
construtor da composição como um todo, enquanto em uma associação os
objetos associados normalmente são criados de maneira independente em
locais diferentes do código (e associados quando necessário).

Um último tipo de relacionamento, a **realização**, ocorre quando uma
classe define que implementa uma determinada interface. Uma
**interface** pode ser vista como uma classe abstrata com todos os
métodos abstratos[^1] e serve como um protocolo entre os clientes e os
implementadores da interface. Nesse caso, a classe (ou uma de suas
subclasses) deve implementar os métodos descritos na interface. Dessa
forma, os clientes podem implementar código que satisfaça a interface
sem se preocupar em como as classes que a implementam o fazem.

[^1]: Em Java, por exemplo, desde a versão 8, é possível definir métodos
    concretos em interfaces, chamados de métodos padrão (através da
    palavra reservada `default`). Neste caso, as classes que implementam
    (realizam) uma interface que possui um método padrão não precisam
    prover implementação para este método (embora possam, caso
    desejado).

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Leia também

- [Classes em Java](/classes-em-java/)
- [Herança em Java](/heranca-em-java/)
- [Polimorfismo em Java](/polimorfismo-em-java/)
- [Interfaces em Java](/interfaces-em-java/)
- [Links POO - Java](/links-poo-java/)
- [Exercícios de Orientação a Objetos](/exercicios-poo-java/)
