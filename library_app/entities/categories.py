from ..database.categories import list_categories

class Topic:
    def __init__(self, name, descripion, subject):
        self._name = name
        self._description = descripion
        self._subject = subject

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
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