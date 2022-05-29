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
        if name in user_dict:
            raise Exception
        else:
            self._name = name

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        for i in user_dict:
            if user_dict[i]["cpf"] == cpf or len(cpf) != 11:
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

    @pendency.setter
    def pendency(self, book):
        if self._role == "STUDENT" or "EMPLOYEE":
            if self._pendency < 3:
                book = book.upper()
                if book not in self._pendency:
                    self._pendency.append(book)
                    return True
                else:
                    return False
        elif self._role == "TEACHER":
            if self._pendency < 5:
                book = book.upper()
                if book not in self._pendency:
                    self._pendency.append(book)
                    return True
                else:
                    return False
        else:
            self._pendency.append(book)

    def login(self, password_input):
        if password_input == self.password:
            return True
        else:
            return False

    # @classmethod
    # def set_user(cls, name, cpf, password, role):
    #     user = User()
    #     user.name = name
    #     user.cpf = cpf
    #     user.password = password
    #     user.role = role
    #     user_dict[user.name] = user