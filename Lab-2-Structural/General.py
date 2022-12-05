from Superior import Superior
import zope.interface

@zope.interface.implementer(Superior)
class General:
    def __init__(self, under_attack):
        self.under_attack = under_attack

    def is_under_attack(self):
        return self.is_under_attack

    def give_order(self, x, y):
        return x, y
