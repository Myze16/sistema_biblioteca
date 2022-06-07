from datetime import datetime, timedelta
from database import loan_dict

class Loan:
    def __init__(self, user, book, exemplary):
        self._user = user
        self._book = book
        self._exemplary = exemplary
        self._inital_date = datetime.now()
        self._final_date = self._inital_date + timedelta(days=10) if user.role == "STUDENT" or user.role == "EMPLOYEE" else self._inital_date + timedelta(days=15)
        loan_dict[self._]= self

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
