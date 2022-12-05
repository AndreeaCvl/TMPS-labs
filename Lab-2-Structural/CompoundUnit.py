import zope.interface
from Unit import Unit

@zope.interface.implementer(Unit)
class CompoundUnit:
    def __init__(self):
        self.unit_list = []

    def add(self, vechicle):
        self.unit_list.append(vechicle)

    def remove(self, index):
        self.unit_list.pop(index)

    def get_position(self):
        return sum([u.get_position()[0] for u in self.unit_list])/len(self.unit_list), sum([u.get_position()[1] for u in self.unit_list])/len(self.unit_list)