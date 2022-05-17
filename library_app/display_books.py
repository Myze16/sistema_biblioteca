class BookDisplay:
    def register_book_topic():
        option = input('''
 ________________________________
|                                |
|         REGISTER BOOK          |
|           AND TOPIC            |
|                         _____  |
|  1- Register Book      |    || |
|  2- Register Exemplary |Book|| |
|  3- Register Topic     |____|| |
|________________________________|
''')
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case _:
                print("Please enter a valid option")


    def consult_book():
        option = print('''
 ____________________________
|                            |
|       CONUSLT BOOK         |
|                         _  |
|   1- Search by name    (_) |
|   3- Search by topic   /   |
|   2- Search by Author      |
|____________________________|
''')
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case _:
                print("Please enter a valid option")