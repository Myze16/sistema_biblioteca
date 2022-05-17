from categories import Topic
from display_books import BookDisplay, Book
from database import book_dict
from book import Book, Examplary

def main():
    display_book = BookDisplay()
    book_dict["a"] = Book("a", 1, "Gabriel", 1, "Juparanã", 2004, "Herror", {
        "1": Examplary("a", 1, "Gabriel", 1, "Juparanã", 2004, "Herror",True),
        "2": Examplary("a", 1, "Gabriel", 1, "Juparanã", 2004, "Herror",True)
    })
    book_dict["b"] = Book('b', 2, "Junin", 1, "Barra do Piraí", 2003, "Thriller", {
        "1": Examplary('b', 2, "Junin", 1, "Barra do Piraí", 2003, "Thriller",True),
        "2": Examplary('b', 2, "Junin", 1, "Barra do Piraí", 2003, "Thriller",True)
    })
    book_dict["c"] = Book("c", 3, "Mizael", 1, "Vassouras", 2002, "Sports", {
        "1": Examplary("c", 3, "Mizael", 1, "Vassouras", 2002, "Sports", True),
        "2": Examplary("c", 3, "Mizael", 1, "Vassouras", 2002, "Sports", True)
    })
    while True:
        display_book.register_book_topic()
        
if __name__ == "__main__":
    main()