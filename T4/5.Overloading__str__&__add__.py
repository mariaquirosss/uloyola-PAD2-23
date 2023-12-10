class Point:

    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y

    # Notice - method __str__ return an String.
    # Redifinig the __str__ method. (overloading)
    def __str__(self) ->str:

        # We can use the function str(), to convert the int to a String.
        return "("+str(self.x)+","+str(self.y)+")"

    # Redifinig the __add__ method. (overloading)
    def __add__(self, otherPoint):

        return Point(self.x + otherPoint.x, self.y + otherPoint.y)


point1=Point(10,3)
point2=Point(3,4)

point1.

# Using print(Object), will call __str__ method.
print(point1)
print(point2)

# Using Add with Overloading
point3 = point1 + point2

print(point3)