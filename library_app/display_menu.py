from book import Book, Examplary
from user import User
from topic import Topic
from display_book import *
from display_topic import *
from database import role_list


def display_menu_admin():
        while True:
            option = input('''
 __________________________
|                          |
|           MENU           |
|                          |
|  1- Consult              |
|  2- Register             |
|  3- Update               |
|  4- Remove               |
|  5- Generate Report      |
|  6- Return               |
|__________________________|

>>> ''')
            match option:
                case "1":
                    consult()
                case "2":
                    register()
                case "3":
                    update()
                case "4":
                    remove()
                case "5":
                    generate_report()
                case "6":
                    break
                case _:
                    print("Please enter a valid option!")
# -------------------------------------------------------------------

def consult():
    while True:
        option = input('''
 _________________________
|                         |
|         CONSULT         |
|                         |
|   1- Book               |
|   2- Exemplary          |
|   3- User               |
|   4- Return             |
|_________________________|

>>> ''')
        match option:
            case "1":
                try:
                    consult_book()
                except:
                    print("Error!")
            case "2":
                try:
                    pass
                    #consult_exemplary()
                except:
                    print("Error!")
            case "3":
                try:
                    pass
                    #consult_user()
                except:
                    print("error!")
            case "4":
                break
            case _:
                print("Please enter a valid option!")
# -------------------------------------------------------------------

def register():
    while True:
        option = input('''
 __________________________
|                          |
|         REGISTER         |
|                          |
|  1- Register book        |
|  2- Register exemplary   |
|  3- Register topic       |
|  4- Register user        |
|  5- Return               |
|__________________________|

>>> ''')
        match option:
            case "1":
                try:
                    title = input("Title: ")
                    isbn = input("Isbn: ")
                    author = input("Author: ")
                    edition = input("Edition: ")
                    publi = input("Publishing company: ")
                    year = input("Year: ")
                    topic = input("Topic: ")
                    book = Book(title, isbn, author, edition, publi, year, topic)
                    print(f"Book {book.title} registered!")
                except:
                    print("Unable to register Book!")
            case "2":
                try:
                    pass
                    #exemplarey = Exemplary.set_info()
                    #print(f"Book {exemplary.title} registered!")
                except:
                    print("Unable to register Exemplary!")
            case "3":
                try:
                    name = input("Name: ")
                    description = input("Descripion: ")
                    subject = input("Subject: ")
                    topic = Topic(name, description, subject)
                    print(f"Topic {topic.name} registered!")
                except:
                    print("Unable to register Topic!")
            case "4":
                try:
                    name = input("Name: ")
                    cpf = input("Cpf: ")
                    password = input("Password: ")
                    print("----Roles----")
                    for i, role in enumerate(role_list):
                        print(role)
                    role = input("Enter the role: ")
                    user = User(name, cpf, password, role)
                    print(f"User {user.name} registered!")
                except:
                    print("Unable to register User!")
            case "5":
                break
            case _:
                print("Please enter a valid option!")
# -------------------------------------------------------------------

def update():
    while True:
        option = input('''
 __________________________
|                          |
|          UPDATE          |
|                          |
|  1- Update book          |
|  2- Update exemplary     |
|  3- Update topic         |
|  4- Update user          |
|  5- Return               |
|__________________________|

>>> ''')
        match option:
            case "1":
                update_book()
            case "2":
                try:
                    pass
                    #exemplarey = Exemplary.set_info()
                    #print(f"Book {exemplary.title} registered!")
                except:
                    print("Unable to register Exemplary!")
            case "3":
                try:
                    update_topic()
                except:
                    print("Unable to register Topic!")
            case "4":
                pass
            case "5":
                break
            case _:
                print("Please enter a valid option!")
# -------------------------------------------------------------------

def remove():
    while True:
        option = input('''
 __________________________
|                          |
|          REMOVE          |
|                          |
|  1- Remove book          |
|  2- Remove exemplary     |
|  3- Remove topic         |
|  4- Remove user          |
|  5- Return               |
|__________________________|

>>> ''')
        match option:
            case "1":
                pass
            case "2":
                 pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Please enter a valid option!")
# -------------------------------------------------------------------

def generate_report():
    while True:
        option = input('''
 __________________________
|                          |
|          REPORT          |
|                          |
|  1- Books report         |
|  2- Borrowed book report |
|  3- Reserved book report |
|  4- Users report         |
|  5- Overdue book report  |
|  6- Return               |
|__________________________|

>>> ''')
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                break
            case _:
                print("Please enter a valid option!")
