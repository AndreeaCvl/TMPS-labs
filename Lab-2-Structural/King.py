import zope.interface
from Superior import Superior
import random

@zope.interface.implementer(Superior)
class King:
    def __init__(self, under_attack):
        self.under_attack = under_attack

    def is_under_attack(self):
        return self.is_under_attack

    def give_order(self, x, y):
        return random.uniform(-0.5, 0.5) + x, random.uniform(-0.5, 0.5) + y
