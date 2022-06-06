from database import loan_dict

def consult_loan():
    while True:
        option = input('''
 ________________________
|                        |
|   CONSULT EXEMPLARY    |
|                        |
|   1- List exemplaries  |
|   2- Search by book    |
|   3- Return            |
|________________________|

>>> ''')
        match option:
            case "1":
                if loan_dict:
                    for exemplary in loan_dict:
                        print(f"{loan_dict[exemplary].book.title} - {loan_dict[exemplary].availability}")

            case "2":
                exemplary_found = False
                search_exemplary_book = input("Enter exemplary name: ")
                for exemplary in loan_dict.values():
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

def update_loan():
    pass
