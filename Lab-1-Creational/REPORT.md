# Lab. 1 - Creational design patterns

This laboratory work contains the implementation of 5 creational 
design patterns:
- Singleton pattern
- Builder pattern
- Factory method
- Abstract factory method
- Prototype pattern

## The singleton Pattern 
A Singleton pattern is a design pattern that allows you to create 
just one instance of a class, throughout the lifetime of a program.
The Library class follows the Singleton pattern. No matter how many
of type Library there would be in our program, the change in one of 
them would affect others too.

## The Builder Pattern
Builder Method is a Creation Design Pattern which aims to “Separate 
the construction of a complex object from its representation so 
that the same construction process can create different 
representations.” It allows you to construct complex objects 
step by step. <br>
The class Book follows the Builder pattern. When creating a new object
of type book, the name, author, cover, and so on must be added step
by step using functions declared in our class.

## The Factory method
 In the Factory pattern, we create objects without exposing the 
 creation logic to the client and the client uses the same common 
 interface to create a new type of object. In this project, it was 
 used to add the feature of translating book titles in 3 different 
 languages. In main.py there is a function which calls the function
 containing the language needed. The logic for translating different
 books can be found in the folder Localizers, classes EnglishLocalizer,
 FrenchLocalizer and RomanianLocalizer.
 
## The Abstract factory method
The Abstract factory method allows you to produce the families of 
related objects without specifying their concrete classes. Using 
the abstract factory method, we have the easiest ways to produce 
a similar type of many objects. In this project it allows 
classifying books by their target audience - children or adults. 
The __init__ function of the Book class can receive a class as 
an argument which then become the hyperparameter age_factory. Setting
its value equal to AdultBooks or ChildrenBooks (both classes) 
allows obtaining the target of a book.

## Prototype pattern
It aims to reduce the number of classes used for an application. 
It allows you to copy existing objects independent of the concrete 
implementation of their classes.  In this project it is used inside
the class PublisherBooks where a function named "clone" is defined
for making exact copies of objects. We can, as shown in main.py, create
a copy of a book which has the same data and has the same publisher,
the only difference being the year of appearence. After we have
the copy, we can modify the needed fields (year) as usual.
