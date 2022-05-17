from book import Book, Examplary
from categories import Topic

def main():
    while True:
        option = input("""
    1 - Register a book
    2 - Register a examplary
    3 - Register a topic
    4 - Return

    Enter the desired option: """)
        match option:
            case "1":
                book = Book.get_info()
                print(f"Book {book.title} created")
            case "2":
                pass
            case "3":
                topic = Topic.get_info()
                print(f"Topic {topic.name} created")
            case _:
                print("Please enter a valid option")


if __name__ == "__main__":
    main()