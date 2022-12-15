# Behavioral Design Patterns

In software engineering, behavioral design patterns have the purpose of identifying common communication patterns between different software entities. By doing so, these patterns increase flexibility in carrying out this communication.

&ensp; &ensp; Some examples from this category of design patterns are :

   * Chain of Responsibility
   * Command
   * Interpreter
   * Iterator
   * Mediator
   * Observer
   * Strategy
   * Memento
   
## Memento Pattern
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without 
revealing the details of its implementation. Memento pattern uses three actor classes. Memento contains state of an object to be restored. Originator creates and stores states in Memento objects and Caretaker object is responsible to restore object state from Memento.
We have created classes `Memento`, `Soldier` (which will act as
the Originator class) and `CareTaker`.

Since the previous project mimicked some kind of RPG game, it would be nice if one could undo the movement of a soldier. This is what are we going to implement below using the Memento Pattern.
```py
class Memento:
    def __init__(self, weapon, name, position, time_served, superior):
        self.weapon = weapon
        self.name = name
        self.position = position
        self.time_served = time_served
        self.superior = superior

    def get_states(self):
        return (self.weapon, self.name, self.position, self.time_served, self.superior)
```
`Memento` implements the `get_states` function which will be used to update the
states of the `Soldier` Originator class.
```py
class CareTaker:
    def __init__(self):
        self.memento_list = []
        self.index = 0
        
    def add(self, state):
        self.memento_list.append(copy.copy(state))

    def undo(self):
        self.index -= 1
        if (self.index < - len(self.memento_list)):
            print("Cannot undo anymore!")
            self.index += 1
            return self.memento_list[self.index]
        return self.memento_list[self.index]
```
The `Soldier` (Originator) class only interacts with the `Memento` class and 
we use the `CareTaker` class to store a list of `Memento` with different states
so we can acces them and therefore restore the Originator's states to some previous
values. Below is the implementation in the `main` class:
```py
king2 = King(under_attack=False)
test_soldier = Soldier(king2, "John", "sword", (0, 0), 5)
care_taker = CareTaker()
care_taker.add(test_soldier.save_states_to_memento())

test_soldier.move(1, 1)
test_soldier.toggle_equip_weapon()
care_taker.add(test_soldier.save_states_to_memento())


test_soldier.move(2, 1)
care_taker.add(test_soldier.save_states_to_memento())

test_soldier.move(1, 3)
care_taker.add(test_soldier.save_states_to_memento())

for i in range(6):
    test_soldier.get_states_from_memento(care_taker.undo())
    print("Undo no. " + str(i + 1) + ":" + str((test_soldier.weapon, test_soldier.position)))
```

As you can see in `main` we only instantiate the `Soldier` and `Caretaker` class.
We use the latter to implement an "undo" functionality to get back to a previous
state of a soldier.