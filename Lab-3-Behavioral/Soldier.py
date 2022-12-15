import zope.interface
from Unit import Unit
import math
import copy
from Memento import Memento

@zope.interface.implementer(Unit)
class Soldier:
    def __init__(self, superior, name, weapon, position, time_served):
        self.weapon = {"name": weapon, "equipped": False}
        self.name = name
        self.position = {"x":position[0], "y":position[1]}
        self.time_served = time_served
        self.superior = superior

    def toggle_equip_weapon(self):
        if (self.superior.is_under_attack()):
            self.weapon["equipped"] = True
        else:
            self.weapon["equipped"] = not self.weapon["equipped"]

    def get_weapon_name(self):
        return self.weapon["name"]

    def get_position(self):
        return tuple(self.position.values())

    def get_name(self):
        return self.name

    def get_time_served(self):
        return self.time_served

    def move(self, x, y):
        direction_vector = self.superior.give_order(x, y)
        self.position["x"] += direction_vector[0]
        self.position["y"] += direction_vector[1]

    def save_states_to_memento(self):
        # we pass a copy of each field to the Memento object because of the way memory allocation works in python
        # if we hadnt passed a copy, any changes to the fields would carry out through to the Memento object
        return Memento(copy.copy(self.weapon), copy.copy(self.name), copy.copy(self.position), copy.copy(self.time_served), copy.copy(self.superior))

    def get_states_from_memento(self, memento):
        self.weapon, self.name, self.position, self.time_served, self.superior = memento.get_states()

