class Shape:
    def __init__(self, shape_name, height):
        self.shape_name = shape_name
        self.shape_height = height

    def __repr__(self):
        return self.shape_name
