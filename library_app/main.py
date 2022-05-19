from display_books import BookDisplay
from fill_database import fill_database

def main():
    display_book = BookDisplay()
    fill_database()
    while True:
        display_book.register_book_topic()
        
if __name__ == "__main__":
    main()