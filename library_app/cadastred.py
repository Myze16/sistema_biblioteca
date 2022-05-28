from categories import Topic
from book import Book, Examplary
from user import User

def cadastred():
    #Users
    User("Junior", "123456", "123","Librarian")
    User("Mizael", "192345", "321", "Clerk")
    User("Gabriel", "928124", "abc", "Manager")
    User("Ana", "193982", "334", "Student")

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