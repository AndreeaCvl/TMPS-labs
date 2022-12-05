import zope.interface
from Unit import Unit
import math

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




