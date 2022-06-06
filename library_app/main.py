from display_user import login_user
from cadastred import cadastred
from display_menu import *


def main():
    cadastred()
    while True:
        user = login_user()
        if user.role == "ADMIN":
            display_menu_admin(user)
        
if __name__ == "__main__":
    main()
    