class Person:
    def __init__(self, name:str, id:str, age: int) -> None:
        self.name =  name
        self.id = id
        self.age = age
        pass
    def copy(self):
        new = Person(self.name,self.id, self.age)
        return new

# Print of John Age
john = Person("John","12345678V",20)
print(f"John age:",john.age)

# Print of a Copy of John
copy = john.copy()
copy.age = 17
print(f"Copy of John age:",copy.age)

# Print of a Reference - John and Luis.
luis = john
john.age = 22
print(f"Luis and John age:",luis.age,john.age)
