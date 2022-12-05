from Soldier import Soldier
import random

class PeasantAdapter(Soldier):
    def __init__(self, peasant):
        self.peasant = peasant

    def toggle_equip_weapon(self):
        pass

    def get_weapon_name(self):
        possible_weapons = ["fists", "pitchfork", "bat"]
        return possible_weapons[random.randint(0, 3)]

    def get_time_served(self):
        return 0