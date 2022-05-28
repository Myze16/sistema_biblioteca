from database import user_dict

class User:
    def __init__(self, name, cpf, password, role):
        self._name = name
        self._cpf = cpf
        self._password = password
        self._role = role
        self._pendency = []
        user_dict[self._name] = self

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def pendency(self):
        return self._pendency

    def set_pendency(self, book):
        book = book.upper()
        if book not in self._pendency:
            self._pendency.append(book)
            return True
        else:
            return False

    def login(self, password_input):
        if password_input == self.password:
            return True
        else:
            return False
