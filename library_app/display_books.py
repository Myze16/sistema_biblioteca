from book import Book
from categories import Topic
from database import book_dict, topic_dict

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
                    topic_dict[topic.name] = topic
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
                    search_book_name = input('Enter book name: ')
                    book_found = False
                    for key in book_dict:
                        if search_book_name.upper() == key.upper():
                            book_found = True
                    if not book_found:
                        print("No books with that name were found!")
                    else:
                        book = book_dict.get(search_book_name.lower())
                        print("-="*20)
                        print(f"Title: {book.title} \nAuthor: {book.author} \nExamplaries: {book.examplary} \nEdition: {book.edition} \nTopic: {book.topic.name} \nPublishing Company: {book.publishing_company} \nYear: {book.year}")
                case "2":
                    search_book_topic = input("Enter book topic: ")
                    book_found = False
                    for book in book_dict.values():
                        if (book.topic.name).upper() == (search_book_topic).upper():
                            book_found = True
                            print("-="*20)
                            print(f"Title: {book.title} \nAuthor: {book.author} \nExamplaries: {book.examplary} \nEdition: {book.edition} \nTopic: {book.topic.name} \nPublishing Company: {book.publishing_company} \nYear: {book.year}")
                    if not book_found:
                        print("No books with that topic were found!")

                case "3":
                    search_book_author = input("Enter boom author: ")
                    book_found = False
                    for book in book_dict.values():
                        if book.author.upper() == search_book_author.upper():
                            book_found = True
                            print("-="*20)
                            print(f"Title: {book.title} \nAuthor: {book.author} \nExamplaries: {book.examplary} \nEdition: {book.edition} \nTopic: {book.topic.name} \nPublishing Company: {book.publishing_company} \nYear: {book.year}")
                        if not book_found:
                            print("No books with that author were found!")
                case "4":
                    break
                case _:
                    print("Please enter a valid option")