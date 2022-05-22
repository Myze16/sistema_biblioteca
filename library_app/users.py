from database import user_dict

class Person:
    def __init__(self, name, cpf, password):
        self._name = name
        self._cpf = cpf
        self._password = password
        user_dict[self._name] = self

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def password(self):
        return self._password


class Reader(Person):
    def __init__(self, name, cpf, password):
        super().__init__(name, cpf, password)
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

    def login(self, password_input):
        if password_input == super().password:
            return True
        else:
            return False


class Employee(Person):
    def __init__(self, name, cpf, password, role):
        super().__init__(name, cpf, password)
        self.__role = role

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    def login(self, password_input):
        if password_input == super().password:
            return True
        else:
            return False