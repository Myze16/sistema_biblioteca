from database import user_dict
from user import User


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
                    user = user_dict.get(name, "")
                    if user.login(password):
                        print(f"\nLogin successfully, welcome {name}!")
                        return user
                    else:
                        print("\nInvalid password!!!")
                else:
                    print("\nInvalid user!!!")
            except:
                print("\nInvalid information")
        case "2":
            print("\nGoing out...")
            exit()
        case _:
            print("\nPlease enter a valid option")

def consult_user():
    while True:
        option = input('''
 ________________________
|                        |
|      CONSULT USER      |
|                        |
|   1- Search by name    |
|   2- Search by role    |
|   3- Search by CPF     |
|   4- Return            |
|________________________|

>>> ''')
        match option:
            case "1":
                search_user_name = input('Enter user name: ')
                user_found = False
                for user in user_dict.values():
                    if user.name.upper() == search_user_name.upper():
                        user_found = True
                        print(f"Name: {user.name} \nRole: {user.role} \nCPF: {user.cpf}")
                    if not user_found:
                        print("No users with that name were found!")
            case "2":
                search_user_role = input("Enter user role: ")
                role_found = False
                for user in user_dict.values():
                    if user.role.upper() == search_user_role.upper():
                        role_found = True
                        print(f"Name: {user.name} \nRole: {user.role} \nCPF: {user.cpf}")
                    if not role_found:
                        print("No users with that role were found!")
            case "3":
                search_user_cpf = input("Enter user cpf: ")
                cpf_found = False
                for user in user_dict.values():
                    if user.cpf.upper() == search_user_cpf.upper():
                        cpf_found = True
                        print(f"Name: {user.name} \nRole: {user.role} \nCPF: {user.cpf}")
                    if not cpf_found:
                        print("No users with that cpf were found!")
            case "4":
                break
            case _:
                print("Please enter a valid option")

