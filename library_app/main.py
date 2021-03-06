from display_user import login_user
from cadastred import cadastred
from display_menu import *


def main():
    cadastred()
    while True:
        user = login_user()
        if user.role == "ADMIN":
            display_menu_admin(user)
        elif user.role == "LIBRARIAN":
            display_menu_librarian(user)
        elif user.role == "EMPLOYEE":
            display_menu_employee(user)
        elif user.role == "STUDENT" or user.role == "TEACHER":
            display_menu_student(user)
        
if __name__ == "__main__":
    main()
    