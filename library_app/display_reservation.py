from database import reservation_dict

def consult_reservation():
    while True:
        option = input('''
 ________________________
|                        |
|   CONSULT RESERVATION  |
|                        |
|   1- List reservations |
|   2- Search by book    |
|   3- Return            |
|________________________|

>>> ''')
        match option:
            case "1":
                if reservation_dict:
                    for exemplary in reservation_dict:
                        print(f"{reservation_dict[exemplary].book.title} - {reservation_dict[exemplary].availability}")
                else:
                    print("Don't have any exemplary!")

            case "2":
                exemplary_found = False
                search_exemplary_book = input("Enter exemplary name: ")
                for exemplary in reservation_dict.values():
                    if exemplary.book.title.upper() == search_exemplary_book.upper():
                        exemplary_found = True
                        print(f"Book: {exemplary.book.title}")
                        print(f"Availability: {exemplary.availability}")
                if not exemplary_found:
                    print("No exemplary of this book was found!")

            case "3":
                break
        
            case _:
                print("Please enter a valid option")

def update_reservation():
    pass
