import zope.interface
from Unit import Unit

@zope.interface.implementer(Unit)
class Peasant():
    def __init__(self, name, position):
        self.name = name
        self.position = {"x": position[0], "y": position[1]}

    def get_position(self):
        return tuple(self.position.values())

    def get_name(self):
        return self.name