from topic import Topic
from book import Book, Exemplary
from user import User

def cadastred():
    #Users
    User("adm", "12678787890", "123", "ADMIN")

    # Topics
    teste = Topic("Drama", "Genero melancolico", "dnfsfsf")
    teste_um = Topic("Drsdfa", "Genero melancolico", "dnfsfsf")
    teste_dois = Topic("rrsdfa", "Genero melancolico", "dnfsfsf")

    # Books
    new_book = Book()
    new_book.title = "Teste Título"
    new_book.isbn = "1234567890123"
    new_book.author = "adm"
    new_book.edition = "1"
    new_book.publishing_company = "UVASS"
    new_book.year = "2022"
    new_book.topic = "Drama"
    

    # Exemplary
    new_exemplary = Exemplary(new_book)