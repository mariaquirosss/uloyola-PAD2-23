class Person:
    def __init__(#TODO):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def set_name(self, name):
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

    def print_info(self):
        #TODO

person = Person("Daniel", "M", 30, "123 Main St", "555-123-4567")
person.print_info()
