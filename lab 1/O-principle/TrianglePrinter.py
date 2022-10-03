from ShapePrinter import ShapePrinter


# TrianglePrinter - contains method for printing triangles. Inherits from the ShapePrinter class
class TrianglePrinter(ShapePrinter):
    def print_shape(self, shape, height):
        print(f'Printing a {shape}:\n')

        k = 1

        for i in range(height):
            print('* ' * k)
            k += 1
