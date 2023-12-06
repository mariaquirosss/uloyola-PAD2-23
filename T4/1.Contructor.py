class Person:

    def __init__(self, name:str, id: str, age: int):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self)-> str:
        return "Name:"+self.name+"\n"+"Id:"+self.id+"\n"+"Age:"+str(self.age)

ManoloObject = Person("Manolo","12345678V",33)
CamelCaseNotation = Person("Luis","22222222J",27)

print(ManoloObject)