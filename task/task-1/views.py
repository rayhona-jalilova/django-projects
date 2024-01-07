from django.shortcuts import render

# Create your views here.
class Car:
    """Person class."""
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def get_car_name(self):
        """Method returns name of a car."""
        return self.name
    
    def get_car_color(self):
        """Method returns color of a car."""
        return self.color
    
car = Car("Mers", "black")
print(car)

"""Class inheritance"""
class Square:
    def __init__(self, color,size) -> None:
        self.color = color
        self.size = size

class Circle:
    def __init__(self, radius, diametr) -> None:
        self.radius = radius
        self.diametr = diametr

class Shape(Square, Circle):
    def get_shape_color(self):
        return self.color
    
    def get_shape_size(self):
        return self.size
    
    def get_shape_radius(self):
        return self.radius
    
    def get_shape_diametr(self):
        return self.diametr
    
shape = Square("white", "15sm",), Circle("5sm", "10sm")
print(shape)

    
        