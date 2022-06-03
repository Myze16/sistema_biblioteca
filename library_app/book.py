from database import book_dict, exemplary_dict, topic_dict

class Book:
    def __init__(self, exemplary={}):
        self._title = None
        self._isbn = None # validar isbn(unico)
        self._author = None
        self._edition = None # Quantas vezes o livro foi publicdo
        self._publishing_company = None
        self._year = None
        self._topic = None
        self._exemplary = {}

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title not in book_dict:
            self._title = title
            book_dict[title] = self
        else:
            raise Exception

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        if len(str(isbn)) == 13:
            self._isbn = isbn
        else:
            raise Exception

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def edition(self):
        return self._edition

    @edition.setter
    def edition(self, edition):
        self._edition = edition
    
    @property
    def publishing_company(self):
        return self._publishing_company

    @publishing_company.setter
    def publishing_company(self, publishing_company):
        self._publishing_company = publishing_company
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year.isnumeric() and len(year) == 4:
            self._year = year
        else:
            raise Exception

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, topic):
        if topic in topic_dict:
            self._topic = topic_dict[topic]
            return True
        else:
            return False
    
    @property
    def exemplary(self):
        return self._exemplary
    
    @exemplary.setter
    def exemplary(self, new_exemplary):
        for exemp in self._exemplary:
            last_id = exemp.id
        if last_id == None:
            last_id = 0
        new_id = last_id + 1
        new_exemplary.id = new_id
        self._exemplary[f"{new_id}"] = new_exemplary

    
class Exemplary(Book):
    def __init__(self, title, isbn, author, edition, publishing_company, year, topic):
        super().__init__(title, isbn, author, edition, publishing_company, year, topic)
        self._id = None
        self._availability = None
        exemplary_dict[self._id] = self
        super().exemplary[self._id] = self

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, availability):
        self._availability = availability