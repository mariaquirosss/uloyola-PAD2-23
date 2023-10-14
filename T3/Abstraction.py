import datetime
import matplotlib

class Person:

    name = "pepe"

    def __init__(self, name, age):
        self.name = name  # Protected attribute
        self.age = 0  # Private attribute
        self.creationTime = datetime.date.today

    def __init__(self, name, age, creationTime):
        self.name = name  # Protected attribute
        self.age = 0  # Private attribute
        self.creationTime = creationTime



    # Public method to get the age (read-only access to the private attribute)
    def get_age(self):
        return self.__age
    

    # Public method to set the age (write access to the private attribute)
    def set_age(self, age):
        if 0 < age <= 120:  # Assuming a reasonable age range
            self.__age = age
        else:
            print("Invalid age value.")

# Create a person
person = Person("Alice")

person1 = Person()


person.set_age()


# Accessing protected attribute directly
print(person._name)  # Accessing protected attribute

person.__creationTime

# Accessing private attribute directly (not recommended)
# This is possible but not a good practice.
# It's better to use the provided methods for accessing and modifying private attributes.
print(person._Person__age)

person.__age = 100
person = Person("Alice", 30)

# Using public methods to access and modify the private attribute
print("Current age:", person.get_age())

person.set_age(35)
print("Updated age:", person.get_age())

person.set_age(150)  # Trying to set an invalid age
