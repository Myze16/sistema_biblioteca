from categories import Topic
from display_books import BookDisplay
from database import book_dict
from cadastred import cadastred
from book import Book, Examplary


def main():
    cadastred()
    display_book = BookDisplay()
    while True:
        display_book.register_book_topic()
        
if __name__ == "__main__":
    main()