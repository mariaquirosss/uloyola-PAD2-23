# Definición de la clase base Publication
class Publication:
    # Constructor de la clase Publication que se ejecuta al crear un nuevo objeto Publication
    def __init__(self, title, authors, year, status="disponible"):
        # Inicialización de los atributos title, authors, year y status del objeto Publication
        self.title = title  # Título de la publicación
        self.authors = authors  # Lista de autores de la publicación
        self.year = year  # Año de publicación
        self.status = status  # Estado de la publicación (disponible por defecto)

# Definición de la clase derivada Book que hereda de la clase Publication
class Book(Publication):
    # Constructor de la clase Book que se ejecuta al crear un nuevo objeto Book
    def __init__(self, title, authors, year, ISBN, num_pages):
        # Llamar al constructor de la clase base Publication para inicializar los atributos title, authors y year
        super().__init__(title, authors, year)
        # Inicialización de los atributos específicos de Book
        self.ISBN = ISBN  # Número de identificación único del libro
        self.num_pages = num_pages  # Número de páginas del libro

# Definición de la clase derivada Journal que hereda de la clase Publication
class Journal(Publication):
    # Constructor de la clase Journal que se ejecuta al crear un nuevo objeto Journal
    def __init__(self, title, authors, year, edition, periodicity):
        # Llamar al constructor de la clase base Publication para inicializar los atributos title, authors y year
        super().__init__(title, authors, year)
        # Inicialización de los atributos específicos de Journal
        self.edition = edition  # Número de edición del periódico
        self.periodicity = periodicity  # Periodicidad del periódico (por ejemplo, mensual)



# Definición de la clase base User
class User:
    # Constructor de la clase User que se ejecuta al crear un nuevo objeto User
    def __init__(self, name, userID):
        # Inicialización de los atributos name y userID del objeto User
        self.name = name  # Nombre del usuario
        self.userID = userID  # Identificación única del usuario
        self.pubs = []  # Lista para almacenar las publicaciones que el usuario ha prestado

    # Método lend_pub que permite al usuario tomar prestada una publicación
    def lend_pub(self, publication):
        # Verificar si el usuario puede tomar prestada la publicación (no ha alcanzado el límite)
        if len(self.pubs) < self.max_pubs:
            # Agregar la publicación a la lista de publicaciones prestadas por el usuario
            self.pubs.append(publication)
            # Cambiar el estado de la publicación a "prestada"
            publication.status = "borrowed"
        else:
            # Imprimir un mensaje si el usuario ha alcanzado el límite máximo de elementos prestados
            print(f"{self.name} ha alcanzado el límite máximo de elementos prestados.")

    # Método return_pub que permite al usuario devolver una publicación prestada
    def return_pub(self, publication):
        # Verificar si la publicación está en la lista de publicaciones prestadas por el usuario
        if publication in self.pubs:
            # Eliminar la publicación de la lista de publicaciones prestadas por el usuario
            self.pubs.remove(publication)
            # Cambiar el estado de la publicación a "disponible"
            publication.status = "available"
        else:
            # Imprimir un mensaje si la publicación no fue prestada por el usuario
            print(f"El libro {publication.title} no fue prestado por {self.name}.")

# Definición de la clase derivada Professor que hereda de la clase User
class Professor(User):
    # Constructor de la clase Professor que se ejecuta al crear un nuevo objeto Professor
    def __init__(self, name, userID, department, employeeID):
        # Llamar al constructor de la clase base User para inicializar los atributos name y userID
        super().__init__(name, userID)
        # Inicialización de los atributos específicos de Professor
        self.department = department  # Departamento al que pertenece el profesor
        self.employeeID = employeeID  # Identificación única del empleado
        self.max_pubs = 2  # Límite máximo de elementos prestados para un profesor

# Definición de la clase derivada Student que hereda de la clase User
class Student(User):
    # Constructor de la clase Student que se ejecuta al crear un nuevo objeto Student
    def __init__(self, name, userID, grade, studentID):
        # Llamar al constructor de la clase base User para inicializar los atributos name y userID
        super().__init__(name, userID)
        # Inicialización de los atributos específicos de Student
        self.grade = grade  # Grado académico del estudiante
        self.studentID = studentID  # Identificación única del estudiante
        self.max_pubs = 1  # Límite máximo de elementos prestados para un estudiante



# Definición de la clase Library
class Library:
    # Constructor de la clase Library
    def __init__(self, name):
        # Atributos de la clase Library
        self.name = name  # Nombre de la biblioteca
        self.catalogue = []  # Lista de objetos de tipo Publication (catálogo de la biblioteca)
        self.users = []  # Lista de objetos de tipo User (usuarios registrados en la biblioteca)

    # Método que muestra el catálogo de la biblioteca
    def show_catalog(self):
        print(f"Catálogo de la biblioteca: {self.name}")
        print("-" * 50)
        for item in self.catalogue:
            print(f"{item.title} - {item.authors} ({item.year})")
        print("-" * 50)

    # Método que agrega una nueva publicación al catálogo
    def add_publication(self, publication):
        self.catalogue.append(publication)

    # Método que registra un nuevo usuario en la biblioteca
    def register_user(self, user):
        self.users.append(user)

    # Método que permite a un usuario tomar prestada una publicación del catálogo
    def lend_pub(self, user, publication):
        # Verificar que tanto el usuario como la publicación estén registrados
        if user in self.users and publication in self.catalogue:
            # Verificar si el usuario puede tomar prestada la publicación
            if len(user.pubs) < user.max_pubs:
                user.lend_pub(publication)  # Llamar al método lend_pub del usuario para realizar el préstamo
                print(f"El libro '{publication.title}' ha sido prestado a {user.name}.")
            else:
                print(f"{user.name} ha alcanzado el límite máximo de elementos prestados.")
        else:
            print("El usuario o la publicación no están registrados.")

    # Método que permite a un usuario devolver una publicación prestada
    def return_pub(self, user, publication):
        # Verificar que tanto el usuario como la publicación estén registrados
        if user in self.users and publication in self.catalogue:
            user.return_pub(publication)  # Llamar al método return_pub del usuario para devolver la publicación
            print(f"El libro '{publication.title}' ha sido devuelto por {user.name}.")
        else:
            print("El usuario o la publicación no están registrados.")


# Example Usage:
library = Library("Loyola Andalucía Library")

book1 = Book("Learning Python II", ["Javier Perez", "Daniel Muñoz"], 2023, "1234567890123", 300)
journal1 = Journal("Technology Journal", ["Stephen Curry", "LeBron James"], 2022, 7, "Annual")
journal2 = Journal("Medical Journal", ["Michael Jordan", "Larry Bird"], 2023, 5, "Monthly")

professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

library.add_publication(book1)
library.add_publication(journal1)
library.add_publication(journal2)

library.register_user(professor1)
library.register_user(student1)

library.show_catalog()

library.lend_pub(professor1, book1)
library.lend_pub(student1, book1)  # the book should be borrowed
print(student1.pubs)  # empty list
library.return_pub(professor1, book1)
library.lend_pub(student1, book1)  # the book should be available now
library.lend_pub(student1, journal2)
print(student1.pubs)
library.lend_pub(student2, journal1)  # User not registered
