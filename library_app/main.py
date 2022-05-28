from categories import Topic
from display_books import BookDisplay
from display_users import UserDisplay
from database import book_dict
from cadastred import cadastred
from book import Book, Examplary


def main():
    cadastred()
    display_book = BookDisplay()
    display_user = UserDisplay()
    while True:
        if display_user.login_user():
            display_book.display_menu()
        
if __name__ == "__main__":
    main()