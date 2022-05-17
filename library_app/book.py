from database import book_dict

class Book:
    def __init__(self, title, isbn, author, edition, publishing_company, year, topic):
        self._title = title
        self._isbn = isbn  # validar isbn(unico)
        self._author = author
        self._edition = edition
        self._publishing_company = publishing_company
        self._year = year
        self._topic = topic
        self._examplary = {}
        book_dict[self._title] = title

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
        self._isbn = isbn
        #book_dict[self._title]['isbn'] = isbn

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
        self._topic = topic

    @classmethod
    def get_info(self):
        title = input("Title: ")
        isbn = input("Isbn: ")
        author = input("Author: ")
        edition = input("Edition: ")
        publi = input("Publishing company: ")
        year = input("Year: ")
        topic = input("Topic: ")
        return Book(title, isbn, author, edition, publi, year, topic)

    
class Examplary(Book):
    def __init__(self, title, isbn, author, edition, publishing_company, year, topic, availability):
        super().__init__(title, isbn, author, edition, publishing_company, year, topic)
        self._id = None
        self._availability = availability

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self):
        if book_dict:
            for i in book_dict:
                if i['id'] > self._id:
                    self._id = i['id'] + 1

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, availability):
        self._availability = availability