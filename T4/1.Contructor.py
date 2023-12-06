class Person:

    def __init__(self, name:str, id: str, age: int) -> Person:
        self.name = name
        self.id = id
        self.age = age


ManoloObject = Person("Manolo","12345678V",33)
CamelCaseNotation = Person("Luis","22222222J",27)