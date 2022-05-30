from categories import Topic
from book import Book, Exemplary
from user import User

def cadastred():
    #Users
    User("adm", "12678787890", "123", "ADMIN")

    # Topics
    Topic("Drama", "Genero melancolico", "dnfsfsf")
    Topic("Drsdfa", "Genero melancolico", "dnfsfsf")
    Topic("rrsdfa", "Genero melancolico", "dnfsfsf")

    # Books
    Book("Borboleta", 1238172, "Douglas Natalino", "Jardim colorido", "Intriseca", 2022, "Drama")
    Book("Xarara", 1238332, "Junior Nascmento", "Jardim Escuro", "Intriseca", 2022, "Drama")
    Book("Mariposa", 1238174, "Douglas Renato", "Jardineiro", "Intriseca", 2022, "Drama")

    # Exemplary
    Exemplary("Borbole21a", 1238172, "Douglas Natalino", "Jardim colorido", "Intriseca", 2022, "Drama")
    Exemplary("B212313boleta", 1238172, "Douglas Natalino", "Jardim colorido", "Intriseca", 2022, "Drama")
    Exemplary("gagagagaeta", 1238172, "Douglas Natalino", "Jardim colorido", "Intriseca", 2022, "Drama")
