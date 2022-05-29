from database import topic_dict

class Topic:
    def __init__(self, name, description, subject):
        self._name = name
        self._description = description
        self._subject = subject
        topic_dict[name] = self

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        topic_dict[name] = topic_dict[self._name]
        del topic_dict[self._name]
        self._name = name

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @classmethod
    def set_info(cls):
        name = input("Name: ")
        description = input("Descripion: ")
        subject = input("Subject: ")
        return Topic(name, description, subject)