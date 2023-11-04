import math;

class Person:
    def __init__(self, name, surname, age, address, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def copy(self):
        new = Person(self.name, self.surname, self.address, self.phone_number)
        return new

    def __del__(self):
        print("Destructor called")


    def get_name(self):
        return self.name

    def set_name(self, name:str)->None:
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

# Example usage of the Person class:
person = Person("Daniel", "M", 30, "123 Main St", "555-123-4567")
person1 = Person("Daniel", "M", 30, "123 Main St", 123456)

copy = person
copy.age = 18

print(person.get_age())

person.__repr__()
person.__str__()

value = math.pi

value.

print(value.__str__())

person1.__del__()

# You can also use the getters and setters to access and modify attributes:
person.set_age(35)
print(f"Updated Age: {person.get_age()}")