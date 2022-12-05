import zope.interface

class Unit(zope.interface.Interface):
    def get_position(self):
        pass