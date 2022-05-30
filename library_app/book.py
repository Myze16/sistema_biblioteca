from database import book_dict, exemplary_dict, topic_dict

class Book:
    def __init__(self, title, isbn, author, edition, publishing_company, year, topic, exemplary={}):
        self._title = title
        self._isbn = isbn  # validar isbn(unico)
        self._author = author
        self._edition = edition # Quantas vezes o livro foi publicdo
        self._publishing_company = publishing_company
        self._year = year
        self._topic = topic
        self._exemplary = {}
        book_dict[self._title] = self

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title in book_dict:
            return False
        else:
            book_dict[title] = book_dict[self._title]
            del book_dict[self._title]
            self._title = title

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        if vars(self)['isbn'] == isbn:
            return False
        else:
            return True

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
        self._year = year

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, topic):
        if topic in topic_dict:
            self._topic = topic
            return True
        else:
            return False
    
    @property
    def exemplary(self):
        return self._exemplary
    
    @exemplary.setter
    def exemplary(self, exemplary):
        self._exemplary[exemplary.id] = exemplary

    @classmethod
    def get_info(cls):
        title = input("Title: ")
        isbn = input("Isbn: ")
        author = input("Author: ")
        edition = input("Edition: ")
        publi = input("Publishing company: ")
        year = input("Year: ")
        topic = input("Topic: ")
        return Book(title, isbn, author, edition, publi, year, topic)

    
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