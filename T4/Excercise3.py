import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        return Point(self._y, self._x)

    def distance_to(self, other_point):
        return math.sqrt((self._x - other_point.x)**2 + (self._y - other_point.y)**2)

    def __str__(self):
        return f"({self._x}, {self._y})"

class Rectangle():
    def __init__(self, point1, point2):
        self._point1 = point1 
        self._point2 = point2 

    @property
    def area(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return width * height

    @property
    def perimeter(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return 2 * (width + height)

# Test program
point1 = Point(1, 2)
point2 = Point(3, 5)
point3 = point1.invert_coordinates()
point4 = point2.invert_coordinates()

rectangle = Rectangle(point1, point2)

print("Rectangle Area:", rectangle.area)
print("Rectangle Perimeter:", rectangle.perimeter)

# Extract x and y coordinates of the points
x_values = [point1.x, point2.x, point3.x, point4.x]
y_values = [point1.y, point2.y, point3.y, point4.y]

# Plot the rectangle
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.fill(x_values, y_values, alpha=0.3)  # Fill the rectangle with some transparency

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Rectangle Visualization')

# Show the plot
plt.grid(True)
plt.show()
