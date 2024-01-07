"""Class inheritance"""
class Shape(Square, Circle):
    def get_shape_color(self):
        return self.color
    
    def get_shape_size(self):
        return self.size
    
    def get_shape_radius(self):
        return self.radius
    
    def get_shape_diametr(self):
        return self.diametr
    
class Square:
    def __init__(self, color,size) -> None:
        self.color = color
        self.size = size

class Circle:
    def __init__(self, radius, diametr) -> None:
        self.radius = radius
        self.diametr = diametr


    
shape = Square("white", "15sm",), Circle("5sm", "10sm")
print(shape)