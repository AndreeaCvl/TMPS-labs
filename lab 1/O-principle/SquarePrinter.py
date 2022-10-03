from ShapePrinter import ShapePrinter


# SquarePrinter - contains method for printing squares. Inherits from the ShapePrinter class
class SquarePrinter(ShapePrinter):
    def print_shape(self, shape, height):
        print(f'Printing a {shape}:\n')

        for i in range(height):
            print('* ' * height)
