from Soldier import Soldier
import math

class Mercenary(Soldier):
    def __init__(self, superior, name, weapon, position, time_served):
        super().__init__(superior, name, weapon, position, time_served)
        self.base_pay = 500

    def get_pay(self):
        return self.base_pay + self.time_served * 10


