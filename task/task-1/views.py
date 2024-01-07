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