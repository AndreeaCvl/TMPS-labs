from ShapePrinter import ShapePrinter


# RectanglePrinter - contains method for printing rectangles. Inherits from the ShapePrinter class
class RectanglePrinter(ShapePrinter):
    def print_shape(self, shape, height):
        print(f'Printing a {shape}:\n')

        for i in range(height):
            print(' * ' * height * 2)