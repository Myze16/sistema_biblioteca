from datetime import datetime, timedelta
from database import reservation_dict

class Reservation:
    def __init__(self, user, book, initial_date, exemplary):
        self._user = user
        self._book = book
        self._exemplary = exemplary
        self._initial_date = initial_date
        self._final_date = initial_date + timedelta(days=10)
        self._id = int(list(reservation_dict.keys())[-1]) + 1 if reservation_dict else 0
        self._exemplary.availability = False
        reservation_dict[self._id] = self

    @property
    def book(self):
        return self._book

    @property
    def initial_date(self):
        return self._initial_date

    @property
    def final_date(self):
        return self._final_date

    @property
    def user(self):
        return self._user

    @classmethod
    def convert_date(cls, year, month, day):
        return datetime(year, month, day)
    
    @classmethod
    def verify_exemplary(cls, book):
        available_exemplary = False
        for exemplary in book.exemplary.values():
            if exemplary.availability:
                available_exemplary = True
                return exemplary
        if not available_exemplary:
            raise Exception
