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
''')
        match option:
            case "1":
                pass
            case "2":
                pass
            case _:
                print("Please enter a valid option")


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
''')
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


