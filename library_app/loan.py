class Loan:
    def __init__(self, book, initial_date):
        self._book = book
        self._initial_date = initial_date
        self._final_date = initial_date + 10
    
    @property
    def book(self):
        return self._book
    
    @property
    def initial_date(self):
        return self._initial_date

    @property
    def final_date(self):
        return self._final_date