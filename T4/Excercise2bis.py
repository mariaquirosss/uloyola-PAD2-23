import math

class Point:
    def __init__(self, x, y):
        # TODO
        # TODO

    @property
    def x(self) -> float:
        # TODO

    @x.setter
    def x(self, value):
        # TODO

    @property
    def y(self) -> float:
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

def main():

    # Test program
    point = Point(2, 3)
    print("Point:", point)
    print("Value X Coordinate:", point.x)

    point.x = 0
    print("X coordinate updated to 0:", point)

if __name__ ==  "__main__":
    main()

