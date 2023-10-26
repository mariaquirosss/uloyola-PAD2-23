from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self):
        self.area = 10
        self.perimeter = None

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Square(Figure):
    def __init__(self, #TODO):
        

    def calculate_area(self):
        #TODO

    def calculate_perimeter(self):
        #TODO


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width

    def calculate_area(self):
        self.area = self.width * self.height

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)

# Example usage:
rectangle = Rectangle(5, 7)
rectangle.calculate_area()
rectangle.calculate_perimeter()
print(f"Rectangle - Area: {rectangle.area}, Perimeter: {rectangle.perimeter}")