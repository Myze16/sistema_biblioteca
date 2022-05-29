from book import Book, Examplary
from categories import Topic
from database import book_dict, topic_dict



class BookDisplay:
    def display_menu_admin(self):
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
                    self.consult()
                case "2":
                    self.register()
                case "3":
                    pass
                    #self.update()
                case "4":
                    pass
                    #self.remove()
                case "5":
                    pass
                    #self.generate_report()
                case "6":
                    break
                case _:
                    print("Please enter a valid option!")

# -------------------------------------------------------------------

    def register(self):
        while True:
            option = input('''
     __________________________
    |                          |
    |         REGISTER         |
    |                          |
    |  1- Register Book        |
    |  2- #Register Exemplary  |
    |  3- Register Topic       |
    |  4- Return               |
    |__________________________|

>>> ''')
            match option:
                case "1":
                    try:
                        book = Book.get_info()
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
                        topic = Topic.set_info()
                        print(f"Topic {topic.name} registered!")
                    except:
                        print("Unable to register Topic!")
                case "4":
                    break
                case _:
                    print("Please enter a valid option!")

# -------------------------------------------------------------------

    def consult(self):
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
                        self.consult_book()
                    except:
                        print("Error!")
                case "2":
                    try:
                        pass
                        #self.consult_exemplary()
                    except:
                        print("Error!")
                case "3":
                    try:
                        pass
                        #self.consult_user()
                    except:
                        print("error!")
                case "4":
                    break
                case _:
                    print("Please enter a valid option!")

# -------------------------------------------------------------------

    def update(self):
        while True:
            option = input('''
     __________________________
    |                          |
    |         REGISTER         |
    |                          |
    |  1- #Update Book         |
    |  2- #Update Exemplary    |
    |  3- Update Topic         |
    |  4- Return               |
    |__________________________|

>>> ''')
            match option:
                case "1":
                    try:
                        book = Book.get_info()
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
                        self.topic_display.update()
                    except:
                        print("Unable to register Topic!")
                case "4":
                    break
                case _:
                    print("Please enter a valid option!")

# -------------------------------------------------------------------

    def consult_book(self):
        while True:
            option = input('''
     _________________________
    |                         |
    |      CONSULT BOOK       |
    |                         |
    |   1- Search by name     |
    |   2- Search by topic    |
    |   3- Search by Author   |
    |   4- Return             |
    |_________________________|
    
>>> ''')
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
                        book = book_dict[search_book_name]
                        print(f"Title: {book.title} \nAuthor: {book.author} \nExamplaries: {book.examplary} \nTopic: {book.topic} \nYear: {book.year}")
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

# -------------------------------------------------------------------
