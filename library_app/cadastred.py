from categories import Topic
from book import Book, Examplary
from users import Employee, Reader

def cadastred():
    #Users
    Employee("Junior", "123456", "123","Librarian")
    Employee("Mizael", "192345", "321", "Clerk")
    Employee("Gabriel", "928124", "abc", "Manager")
    Reader("Ana", "193982", "334")

    # Topics
    Topic("Drama", "Genero melancolico", "dnfsfsf")
    Topic("Drsdfa", "Genero melancolico", "dnfsfsf")
    Topic("rrsdfa", "Genero melancolico", "dnfsfsf")


    # Books
    Book("Borboleta", 1238172, "Douglas Natalino", "Jardim colorido", "Intriseca", 2022, "Drama")
    Book("Xarara", 1238332, "Junior Nascmento", "Jardim Escuro", "Intriseca", 2022, "Drama")
    Book("Mariposa", 1238174, "Douglas Renato", "Jardineiro", "Intriseca", 2022, "Drama")


    # Exemplary
    # Examplary("")