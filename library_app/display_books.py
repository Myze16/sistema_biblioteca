from book import Book
from categories import Topic
from database import book_dict

class BookDisplay:
    def register_book_topic(self):
        while True:
            option = input('''
     ________________________________
    |                                |
    |         REGISTER BOOK          |
    |           AND TOPIC            |
    |                         _____  |
    |  1- Register Book      |    || |
    |  2- Register Exemplary |Book|| |
    |  3- Register Topic     |____|| |
    |  4- Consult Book               |
    |  5- Return                     |
    |________________________________|
    ''')
            match option:
                case "1":
                    book = Book.get_info()
                    print(f"Book {book.title} registered")
                    book_dict[book.title] = book
                case "2":
                    pass
                case "3":
                    topic = Topic.get_info()
                    print(f"Topic {topic.name} registered")
                case "4":
                    self.consult_book()
                case "5":
                    break
                case _:
                    print("Please enter a valid option")


    def consult_book(self):
        while True:
            option = input('''
     ____________________________
    |                            |
    |       CONSULT BOOK         |
    |                         _  |
    |   1- Search by name    (_) |
    |   2- Search by topic   /   |
    |   3- Search by Author      |
    |   4- Return                |
    |____________________________|
    ''')
            match option:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    break
                case _:
                    print("Please enter a valid option")