from abc import ABC, abstractmethod

# Create an abstract base class for animals
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

# Create concrete classes for different types of animals
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Donkey(Animal):
    def speak(self):
        return f"{self.name} says Buuu!"



if __name__ ==  "__main__":
    # Create instances of concrete animal types
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    myDonkey = Donkey("Pepe")

    #
    print(dog.speak())  # Buddy says Woof!
    print(cat.speak())  # Whiskers says Meow!
    print(myDonkey.speak())
