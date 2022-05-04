class Person:
    def __init__(self, name, cpf):
        self._name = name
        self._cpf = cpf


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

    def get_name(self):
        return super()._name

    def get_cpf(self):
        return super()._cpf

    def get_pendency(self):
        return self.__pendency


class Employee(Person):
    def __init__(self, name, cpf, role):
        super().__init__(name, cpf)
        self.__role = role

    def set_role(self, role):
        self.__role = role

    def get_name(self):
        return super()._name

    def get_cpf(self):
        return super()._cpf

    def get_role(self):
        return self.__role