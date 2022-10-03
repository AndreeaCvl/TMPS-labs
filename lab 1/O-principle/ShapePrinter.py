# Abstract class ShapePrinter containing an abstract method or printing different shapes
from abc import abstractmethod, ABC


class ShapePrinter(ABC):
    @abstractmethod
    def print_shape(self, shape, height):
        pass
