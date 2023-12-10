import math

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        self._x, self._y = self._y, self._x

    def distance_to(self, other_point):
        distanceX = self._x - other_point._x
        distanceY = self._y - other_point._y
        return math.sqrt(distanceX**2 + distanceY**2)

    def __str__(self):
        return f"({self._x}, {self._y})"

def main():

    # Test program
    point = Point(2, 3)
    print("Point:", point)
    print("Value X Coordinate:", point.x)

    point.x = 0
    print("X coordinate updated to 0:", point)

    point.invert_coordinates()
    print(f"Coordinates inverted {point}")

    newPoint = Point(5,5)

    print(f"Distance "+str(point.distance_to(newPoint)))


if __name__ ==  "__main__":
    main()

