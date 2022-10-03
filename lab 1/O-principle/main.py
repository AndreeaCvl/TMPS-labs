from Shape import Shape
from TrianglePrinter import TrianglePrinter
from RectanglePrinter import RectanglePrinter
from SquarePrinter import SquarePrinter


# runner code
if __name__ == '__main__':
    shape = Shape('Square', 5)
    screen = SquarePrinter()
    screen.print_shape(shape, shape.shape_height)
