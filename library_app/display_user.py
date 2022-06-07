from database import user_dict, role_list
from user import User


def login_user():
    while True:
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

def update_user():
    while True:
        option = input('''
 __________________________
|                          |
|          UPDATE          |
|                          |
|  1- List users           |
|  2- Update name          |
|  3- Update cpf           |
|  4- Update password      |
|  5- Update role          |
|  6- Return               | 
|__________________________|

>>> ''')
        match option:
            case "1":
                try:
                    if user_dict:
                        for user in user_dict:
                            print(f"{user_dict[user].name} - {user_dict[user].cpf} - {user_dict[user].role}")
                except:
                    print("There are no users registered!")
            case "2":
                try:
                    user = input("Enter user name: ")
                    user = user_dict[user]
                    new_name = input("Enter new user name: ")
                    user.name = new_name
                    print(f"New name {user.name} successfully applied!")
                except:
                    print("User not found!")
            case "3":
                try:
                    user = input("Enter user name: ")
                    user = user_dict[user]
                    new_cpf = input("Enter new user cpf: ")
                    user.cpf = new_cpf
                    print(f"New cpf {user.cpf} successfully applied!")
                except:
                    print("User not found!")
            case "4":
                try:
                    user = input("Enter user name: ")
                    user = user_dict[user]
                    new_password = input("Enter new user password: ")
                    user.password = new_password
                    print(f"New password {user.password} successfully applied!")
                except:
                    print("User not found!")
            case "5":
                try:
                    user = input("Enter user name: ")
                    user = user_dict[user]
                    print("----Roles----")
                    for i, role in enumerate(role_list):
                        print(role)
                    new_role = input("Enter new user role: ")
                    user.role = new_role
                    print(f"New role {user.role} successfully applied!")
                except:
                    print("User not found!")
            case "6":
                break
            case _:
                print("Please enter a valid option!")

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
