from Person import Person

class Client(Person):
    def __init__(self, name, lastname, document, tel, category):
        super().__init__(name, lastname, document, tel)
        self.category = category