import math

class Point:
    def __init__(self, x, y):
        # TODO
        # TODO

    @property
    def x(self):
        # TODO

    @x.setter
    def x(self, value):
        # TODO

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        # TODO

    def distance_to(self, other_point):
        # TODO

    def __str__(self):
        return f"({self._x}, {self._y})"

# Test program
point = Point(3, 4)
print("Point:", point)
print("X Coordinate:", point.x)

point.x = 0
print("After setting X coordinate to 0:", point)
