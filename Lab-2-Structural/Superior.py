import zope.interface

class Superior(zope.interface.Interface):
    def __init__(self, x):
        pass
    def is_under_attack(self):
        pass
    def give_directions(self, x, y):
        pass