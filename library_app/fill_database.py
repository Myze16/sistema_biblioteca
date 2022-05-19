from database import topic_dict, book_dict
from book import Book, Examplary
from categories import Topic

def fill_database():

    topic_dict["horror"] = Topic("Horror", "Description for Horror", "Subject for Horror")
    topic_dict["thriller"] = Topic("Thriller", "Description for Thriller", "Subject for Thriller")
    topic_dict["sports"] = Topic("Sports", "Description for Sports", "Subject for Sports")


    book_dict["a"] = Book("a", 1, "Gabriel", 1, "Juparanã", 2004,topic_dict["horror"], {
        "1": Examplary("a", 1, "Gabriel", 1, "Juparanã", 2004, topic_dict["horror"],True),
        "2": Examplary("a", 1, "Gabriel", 1, "Juparanã", 2004, topic_dict["horror"],True)
    })
    book_dict["b"] = Book("b", 2, "Junin", 1, "Barra do Piraí", 2003, topic_dict["thriller"], {
        "1": Examplary("b", 2, "Junin", 1, "Barra do Piraí", 2003, topic_dict["thriller"],True),
        "2": Examplary("b", 2, "Junin", 1, "Barra do Piraí", 2003, topic_dict["thriller"],True)
    })
    book_dict["c"] = Book("c", 3, "Mizael", 1, "Vassouras", 2002, topic_dict["sports"], {
        "1": Examplary("c", 3, "Mizael", 1, "Vassouras", 2002, topic_dict["sports"], True),
        "2": Examplary("c", 3, "Mizael", 1, "Vassouras", 2002, topic_dict["sports"], True)
    })
