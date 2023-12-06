class A:
    def __init__(self) -> None:
        self.publicA = 10
        self.__privateB = 30
        pass

a = A()

# Public attribute is accesible
print(a.publicA)

# Private attibute should NOT be accesible directly.
print(a.__privateB)