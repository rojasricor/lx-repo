class Person:
    def __init__(self, name, lastname, document, tel):
        self.name = name
        self.lastname = lastname
        self.document = document
        self.tel = tel

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.document + ' ' + self.tel

    # __str__ = lambda self: self.name + ' ' + self.lastname + ' ' + self.document + ' ' + self.tel


