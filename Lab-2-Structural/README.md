# Structural Design Patterns

Structural design pattern is a blueprint of how different objects 
and classes are combined together to form a bigger structure for 
achieving multiple goals altogether. <br>
In this project 3 Structural Design Patterns were implemented:
- Adapter Pattern
- Bridge Pattern
- Composite pattern

The Laboratory work implements some of the logic of an RPG game.

## Adapter Pattern
Adapter is a structural design pattern that allows objects with incompatible 
interfaces to collaborate. <br>
We addapt the Peasant class to act as a Soldier by implementing the 
PeasantAdapter class, which has an attribute of type Peasant and 
implements the missing functions. In this way we avoid making the 
Peasant a subclass of Soldier, which is inconvenient.

## Bridge Pattern
The bridge pattern is a design pattern that is meant to "decouple 
an abstraction from its implementation so that the two can vary 
independently". <br>
We want to add Mercenaries, which are a type of Soldier. Moreover, each Soldier or Mercenary has a superior, a King 
or a General, which gives them directions to go to. The king generally gives less precise directions, so the output of
the position might differ from the result one might expect from the input parameters. Moreover, if the King or General
is under attack, the Soldier/Mercenary is forced to keep their weapon toggled on equipped. Normally, for this we would
need to implement MercenaryKing, MercenaryGeneral, SoldierKing, SoldierGeneral classes. To save up on time and lines
of code, we create the Superior interface, which the King and General class implement slightly differently. We then
provide the Soldier constructor with a superior as a parameter. # Then both Soldier and Mercenary (which is a child of
class Soldier) can have access to the functions inside the superior.

```commandline
king_soldier = Soldier(king, "Ian", "mace", (1, 3), 5)
general_mercenary = Mercenary(king, "Albert", "sword", (0, 0), 2)

print("King Soldier Weapon equipped state: " + str(king_soldier.toggle_equip_weapon()))
print("General Mercenary Weapon equipped state: " + str(general_mercenary.toggle_equip_weapon()))
print()

print(king_soldier.get_position())
king_soldier.move(2, 2)
print(king_soldier.get_position())
print()

print(general_mercenary.get_position())
king_soldier.move(2, 2)
print(general_mercenary.get_position())
print(general_mercenary.get_pay())
print()
```

## Composite pattern
Composite pattern is a partitioning design pattern and describes a 
group of objects that is treated the same way as a single instance 
of the same type of object.
<br>
We may want to group certain units together, since they may be part of the same squad. We might also
want to apply functions to the whole squad, for example get the position of the whole squad,
not just a single unit. For this we want to create a Unit interface and make the Soldier, Peasant and
CompoundUnit class implement it. Each instance of CompoundUnit has a list of objects that implement Unit,
even other CompoundUnit objects. In this way we can recursevly call the .estimate_price() function of each object
and calculate the total sum, although the client doesn't see the difference on their side, because the client sees
the same common interface for all classes.
