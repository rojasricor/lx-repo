from Person import Person

class Employee(Person):
    def __init__(self, name, lastname, document, tel, salario):
        super().__init__(name, lastname, document, tel)
        self.salario = salario