from categories import Topic
from display_books import BookDisplay

def main():
    display_book = BookDisplay()
    while True:
        display_book.register_book_topic()
        
if __name__ == "__main__":
    main()