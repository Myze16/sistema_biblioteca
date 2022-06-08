from reservation import Reservation
from topic import Topic
from book import Book, Exemplary
from user import User

def cadastred():
    #Users
    admin = User("tassio", "12678787890", "123", "ADMIN")
    libra = User("tassio2", "12621424141", "123", "LIBRARIAN")
    employ = User("tassio3", "12125241466", "123", "EMPLOYEE")
    student = User("soares", "19234853288", "soso", "STUDENT")

    # Topics
    teste = Topic("Drama", "Genero melancolico", "dnfsfsf")
    teste_um = Topic("Drsdfa", "Genero melancolico", "dnfsfsf")
    teste_dois = Topic("rrsdfa", "Genero melancolico", "dnfsfsf")

    # Books
    new_book = Book()
    new_book.title = "As aventuras de Tássio Sirq"
    new_book.isbn = "1234567890123"
    new_book.author = "Tassio"
    new_book.edition = "1"
    new_book.publishing_company = "UVASS"
    new_book.year = "2008"
    new_book.topic = "Drama"

    new_book2 = Book()
    new_book2.title = "O pequeno Tassio"
    new_book2.isbn = "1234567890124"
    new_book2.author = "Tassio"
    new_book2.edition = "1"
    new_book2.publishing_company = "UVASS"
    new_book2.year = "2010"
    new_book2.topic = "Drama"
    

    # Exemplary
    new_exemplary = Exemplary(new_book)

    # Reservation
    exemplary = Reservation.verify_exemplary(new_book)
    initial_date = Reservation.convert_date(2022, 1, 1)
    new_reservation = Reservation(admin, new_book, initial_date, exemplary)