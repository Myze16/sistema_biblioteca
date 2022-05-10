from ..database.users import list_users

class Person:
    def __init__(self, name, cpf):
        self._name = name
        self._cpf = cpf

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf


class Reader(Person):
    def __init__(self, name, cpf):
        super().__init__(name, cpf)
        self.__pendency = []

    def set_pendency(self, book):
        book = book.upper()
        if book not in self.__pendency:
            self.__pendency.append(book)
            return True
        else:
            return False

    @property
    def pendency(self):
        return self.__pendency


class Employee(Person):
    def __init__(self, name, cpf, role):
        super().__init__(name, cpf)
        self.__role = role

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role