from datetime import datetime, timedelta
from database import loan_dict

class Loan:
    def __init__(self, user, book, exemplary):
        self._user = user
        self._book = book
        self._exemplary = exemplary
        self._id = int(list(book.exemplary.keys())[-1]) + 1 if book.exemplary else 0
        self._inital_date = datetime.now()
        self._final_date = self._inital_date + timedelta(days=10) if user.role == "STUDENT" or user.role == "EMPLOYEE" else self._inital_date + timedelta(days=15)
        loan_dict[self._id] = self
        self._user.insert_pendency(book, self)

    @property
    def user(self):
        return self._user

    @property
    def book(self):
        return self._book
    
    @property
    def exemplary(self):
        return self._exemplary

    @property
    def initial_date(self):
        return self._inital_date

    @property
    def final_date(self):
        return self._final_date
    
    @classmethod
    def verify_exemplary(cls, book):
        available_exemplary = False
        for exemplary in book.exemplary.values():
            if exemplary.availability:
                available_exemplary = True
                return exemplary
        if not available_exemplary:
            raise Exception
