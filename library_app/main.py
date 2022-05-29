from display_users import UserDisplay
from cadastred import cadastred
from display_menu import *


def main():
    cadastred()
    display_user = UserDisplay()
    while True:
        user = display_user.login_user()
        if user.role == "ADMIN":
            display_menu_admin()
        
if __name__ == "__main__":
    main()
    