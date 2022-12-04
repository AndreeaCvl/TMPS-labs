import copy
from abc import ABCMeta


# prototype method. Contains a function named "clone" which makes an exact copy of the object, and functions set_id
# and get_id allowing the existence of multiple genres.
class PublisherBooks(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None
        self.title = None
        self.year = None

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)