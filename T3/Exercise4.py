import math

# Create the abstract class Figure
class Figure:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

# Square class
class Square(Figure):
    def __init__(self, side=1):
        super().__init__()
        self.side = side

    def calculate_area(self):
        self.area = self.side * self.side

    def calculate_perimeter(self):
        self.perimeter = 4 * self.side

#  Circle class
class Circle(Figure):
    def __init__(self, radius=1):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        self.area = math.pi * self.radius**2

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius

# Triangle class 
class Triangle(Figure):
    def __init__(self, side=1):
        super().__init__()
        self.side = side

    def calculate_area(self):
        height = (math.sqrt(3) / 2) * self.side  
        self.area = (self.side * height) / 2

    def calculate_perimeter(self):
        self.perimeter = 3 * self.side

# rectangle class
class Rectangle(Figure):
    def __init__(self, height=1, width=1):
        super().__init__()
        self.height = height
        self.width = width

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

if __name__ == "__main__":
    square = Square(5)
    square.calculate_area()
    square.calculate_perimeter()
    print("Square Area:", square.area)
    print("Square Perimeter:", square.perimeter)

    circle = Circle(3)
    circle.calculate_area()
    circle.calculate_perimeter()
    print("Circle Area:", circle.area)
    print("Circle Perimeter:", circle.perimeter)

    triangle = Triangle(4)
    triangle.calculate_area()
    triangle.calculate_perimeter()
    print("Triangle Area:", triangle.area)
    print("Triangle Perimeter:", triangle.perimeter)

    rectangle = Rectangle(6, 8)
    rectangle.calculate_area()
    rectangle.calculate_perimeter()
    print("Rectangle Area:", rectangle.area)
    print("Rectangle Perimeter:", rectangle.perimeter)

