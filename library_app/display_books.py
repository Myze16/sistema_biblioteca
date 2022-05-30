from book import Book, Exemplary
from categories import Topic
from database import book_dict, topic_dict


def update_book():
    while True:
        option = input('''
 __________________________
|                          |
|          UPDATE          |
|                          |
|  1- List books           |
|  2- Update title         |
|  3- Update author        |
|  4- Update pub. company  |
|  5- Update year          |
|  6- Update topic         |
|  7- Return               | 
|__________________________|

>>> ''')
        match option:
            case "1":
                try:
                    if book_dict:
                        for book in book_dict:
                            print(f"{book_dict[book].title} - {book_dict[book].author}")
                except:
                    print("There are no books registered!")
            case "2":
                try:
                    book = input("Enter book title: ")
                    book = book_dict[book]
                    new_title = input("Enter new book title: ")
                    book.title = new_title
                    print(f"New title {book.title} successfully applied!")
                except:
                    print("Book not found!")
            case "3":
                try:
                    book = input("Enter book title: ")
                    book = book_dict[book]
                    new_author = input("Enter new book author: ")
                    book.author = new_author
                    print(f"New author {book.author} successfully applied!")
                except:
                    print("Book not found!")
            case "4":
                try:
                    book = input("Enter book title: ")
                    book = book_dict[book]
                    new_pub_company = input("Enter new book publishing company: ")
                    book.publishing_company = new_pub_company
                    print(f"New publishing  {book.publishing_company} successfully applied!")
                except:
                    print("Book not found!")
            case "5":
                try:
                    book = input("Enter book title: ")
                    book = book_dict[book]
                    new_year = input("Enter new book year: ")
                    book.year = new_year
                    print(f"New year {book.year} successfully applied!")
                except:
                    print("Book not found!")
            case "6":
                pass
            case "7":
                break
            case _:
                print("Please enter a valid option")

def consult_book():
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
                search_book_author = input("Enter book author: ")
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