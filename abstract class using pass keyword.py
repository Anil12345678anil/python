from abc import ABC, abstractmethod

# Parent class 1 with abstract method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Parent class 2
class Color:
    def display_color(self, color):
        print("Color:", color)

# Child class inheriting from Shape and Color
class Square(Shape, Color):
    def area(self, side):
        return side * side

# Create object
square = Square()

# Test
print("Square Area:", square.area(4))
square.display_color("Blue")
