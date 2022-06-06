from database import exemplary_dict

def update_exemplary():
    pass

def consult_exemplary():
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
                if exemplary_dict:
                    for exemplary in exemplary_dict:
                        print(f"{exemplary_dict[exemplary].book.title} - {exemplary_dict[exemplary].availability}")

            case "2":
                exemplary_found = False
                search_exemplary_book = input("Enter exemplary name: ")
                for exemplary in exemplary_dict.values():
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
