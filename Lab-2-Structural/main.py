from Soldier import Soldier
from Peasant import Peasant
from PeasantAdapter import PeasantAdapter
from Superior import *
from General import *
from King import King
from Mercenary import Mercenary
from CompoundUnit import CompoundUnit

king = King(under_attack=True)
general = General(under_attack=False)

soldier = Soldier(king, "John", "sword", (0, 0), 10)
peasant = Peasant("Isaac", (0, 0))

# Adapter pattern
# We addapt the Peasant class to act as a Soldier by implementing the PeasantAdapter class,
# which has an attribute of type Peasant and implements the missing functions. In this way
# we avoid making the Peasant a subclass of Soldier, which is inconvenient.

# following code will throw error because a Peasant has no time_served, get_weapon_name and toggle_equip_weapon methods
try:
    print(peasant.get_time_served())
    print(peasant.get_weapon_name())
    peasant.toggle_equip_weapon()
except AttributeError as err:
    print(f"Attribute Error: {err}")

adapt_peasant = PeasantAdapter(peasant)

print("Time served: " + str(adapt_peasant.get_time_served()))
print("Weapon name: " + adapt_peasant.get_weapon_name())

# Bridge pattern
# We want to add Mercenaries, which are a type of Soldier. Moreover, each Soldier or Mercenary has a superior, a King
# or a General, which gives them directions to go to. The king generally gives less precise directions, so the output of
# the position might differ from the result one might expect from the input parameters. Moreover, if the King or General
# is under attack, the Soldier/Mercenary is forced to keep their weapon toggled on equipped. Normally, for this we would
# need to implement MercenaryKing, MercenaryGeneral, SoldierKing, SoldierGeneral classes. To save up on time and lines
# of code, we create the Superior interface, which the King and General class implement slightly differently. We then
# provide the Soldier constructor with a superior as a parameter. # Then both Soldier and Mercenary (which is a child of
# class Soldier) can have access to the functions inside the superior.

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

# Composite pattern
# We may want to group certain units together, since they may be part of the same squad. We might also
# want to apply functions to the whole squad, for example get the position of the whole squad,
# not just a single unit. For this we want to create a Unit interface and make the Soldier, Peasant and
# CompoundUnit class implement it. Each instance of CompoundUnit has a list of objects that implement Unit,
# even other CompoundUnit objects. In this way we can recursevly call the .estimate_price() function of each object
# and calculate the total sum, although the client doesn't see the difference on their side, because the client sees
# the same common interface for all classes.

group1 = CompoundUnit()
group2 = CompoundUnit()
u_list1 = [Soldier(king, "John", "sword", (0, 0), 5), Mercenary(king, "Razvan", "sword", (1, 1), 10), Peasant("John2", (1, 0))]
u_list2 = [Peasant("Adam", (4, 4)), Soldier(general, "Mason", "spear", (1, 1), 8)]

for item in u_list1:
    group1.add(item)

for item in u_list2:
    group2.add(item)

group2.add(group1)

print("Group 2 position:")
print(group2.get_position())