from time import sleep
from database import role_list, user_dict

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
        user_dict[name] = user_dict[self._name]
        del user_dict[self._name]
        self._name = name

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        for user in user_dict:
            if user_dict[user].cpf == cpf or len(cpf) != 11:
                raise Exception
            else:
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
        if role.upper() in role_list:
            self._role = role.upper()
        else:
            raise Exception

    @property
    def pendency(self):
        return self._pendency

    def get_pendencies(self):
        for loan in self._pendency:
            sleep(0.5)
            print(f"Book: {loan.book.title} \nInitial date: {loan.initial_date} \n{loan.final_date}")
        return False

    def insert_pendency(self, book, loan):
        if self._role == "STUDENT" or self._role == "EMPLOYEE":
            if len(self._pendency) < 3:
                if book.title not in self._pendency:
                    self._pendency.append(loan)
                    return True
                else:
                    return False
        elif self._role == "TEACHER":
            if len(self._pendency) < 5:
                book = book.upper()
                if book.title not in self._pendency:
                    self._pendency.append(loan)
                    return True
                else:
                    return False
        else:
            self._pendency.append(loan)

    def login(self, password_input):
        if password_input == self.password:
            return True
        else:
            return False