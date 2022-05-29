from display_books import BookDisplay
from display_users import UserDisplay
from cadastred import cadastred


def main():
    cadastred()
    display_book = BookDisplay()
    display_user = UserDisplay()
    while True:
        user = display_user.login_user()
        if user.role == "ADMIN":
            display_book.display_menu()
        
if __name__ == "__main__":
    main()
    