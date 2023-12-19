# Importar los módulos necesarios
import math
import matplotlib.pyplot as plt

# Definir una clase Point para representar puntos en un plano
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Definir propiedad x con su setter correspondiente
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # Definir propiedad y con su setter correspondiente
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # Método para invertir las coordenadas x e y
    def invert_coordinates(self):
        return Point(self._y, self._x)

    # Método para calcular la distancia entre dos puntos
    def distance_to(self, other_point):
        return math.sqrt((self._x - other_point.x)**2 + (self._y - other_point.y)**2)

    # Representación en cadena del objeto Point
    def __str__(self):
        return f"({self._x}, {self._y})"

# Definir una clase Rectangle para representar rectángulos
class Rectangle():
    def __init__(self, point1, point2):
        self._point1 = point1 
        self._point2 = point2 

    # Propiedad para calcular y devolver el área del rectángulo
    @property
    def area(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return width * height

    # Propiedad para calcular y devolver el perímetro del rectángulo
    @property
    def perimeter(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return 2 * (width + height)

# Programa de prueba
point1 = Point(1, 2)
point2 = Point(3, 5)
point3 = point1.invert_coordinates()
point4 = point2.invert_coordinates()

rectangle = Rectangle(point1, point2)

# Mostrar área y perímetro del rectángulo
print("Rectangle Area:", rectangle.area)
print("Rectangle Perimeter:", rectangle.perimeter)

# Extraer coordenadas x e y de los puntos
x_values = [point1.x, point2.x, point3.x, point4.x]
y_values = [point1.y, point2.y, point3.y, point4.y]

# Trazar el rectángulo en un gráfico
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.fill(x_values, y_values, alpha=0.3)  # Rellenar el rectángulo con cierta transparencia

# Etiquetas y título del gráfico
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Rectangle Visualization')

# Mostrar el gráfico
plt.grid(True)
plt.show()
