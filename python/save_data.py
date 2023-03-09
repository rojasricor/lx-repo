from Employee import Employee
from Client import Client

def save():
    response = input('Que desea ingresar? E para (Empleado) o C para (Cliente): ')
    name = input('ingrese el name: ')
    lastname = input('ingrese el lastname: ')
    document = input('ingrese el document: ')
    tel = input('ingrese el telefono: ')
    if response == 'E':
        salario = input('ingrese el salario del empleado: ')
        employee = Employee(name, lastname, document, tel, salario)
        people.append(employee)
    elif response == 'C':
        tipo = input('ingrese el tipo del cliente: ')
        client = Client(name, lastname, document, tel, tipo)
        people.append(client)


people = []

save()
save()

for person in people:
    print(person)
