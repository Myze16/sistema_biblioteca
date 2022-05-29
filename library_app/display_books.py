from book import Book, Examplary
from categories import Topic
from database import book_dict, topic_dict


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