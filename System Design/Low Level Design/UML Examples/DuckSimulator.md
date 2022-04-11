# The Strategy Pattern

It defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.

For example, in the below diagram, the behavior classes (FlyBehavior and QuackBehavior) can vary independently from the Duck class.

## Some key points to remember
- Identify the aspects of your application that vary and separate them from what stays the same
- Program to an interface, not an implementation
- Favor composition over inheritance

```mermaid
classDiagram

Duck <|-- MallardDuck 
Duck <|-- RedheadDuck
Duck <|-- RubberDuck
Duck <|-- DecoyDuck

Duck --* FlyBehavior
Duck --* QuackBehavior

class Duck {
  +FlyBehavior fb
  +QuackBehavior qb
  +swim()
  +display()
  +setFlyBehavior()
  +setQuackBehavior()
  +performFly()
  +performQuack()
}
class MallardDuck {
  +display()
}
class RedheadDuck {
  +display()
}
class RubberDuck {
  +display()
}
class DecoyDuck {
  +display()
}

class FlyBehavior {
  <<interface>>  
}
class FlyWithWings {
  +fly()
}
class FlyNoWay {
  +fly()
}
FlyBehavior <|.. FlyWithWings
FlyBehavior <|.. FlyNoWay

class QuackBehavior {
  <<interface>>
}
class Quack {
  +quack()
}
class Squeak {
  +quack()
}
class MuteQuack {
  +quack()
}

QuackBehavior <|.. Quack
QuackBehavior <|.. Squeak
QuackBehavior <|.. MuteQuack

```