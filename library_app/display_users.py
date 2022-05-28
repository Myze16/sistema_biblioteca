from database import user_dict
from user import User

class UserDisplay:
    def login_user():
        option = input('''
 ________________
|                |
|     LOGIN      |
|                |
|   1- Sign in   |
|   2- Exit      |
|________________|

>>> ''')
        match option:
            case "1":
                name = input("Name: ")
                password = input("Password: ")
                try:
                    if name in user_dict:
                        user = user_dict[name]
                        if user.login(password):
                            print(f"\nLogin successfully, welcome {name}!")
                            return True
                        else:
                            print("\nInvalid password!!!")
                    else:
                        print("\nInvalid user!!!")
                except:
                    print("\nInvalid information")
            case "2":
                return False
            case _:
                print("\nPlease enter a valid option")

    def consult_user():
        option = input('''
 ________________________
|                        |
|      CONUSLT USER      |
|                        |
|   1- Search by name    |
|   3- Search by role    |
|   2- Search by CPF     |
|   4- Return            |
|________________________|

>>> ''')
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case _:
                print("Please enter a valid option")