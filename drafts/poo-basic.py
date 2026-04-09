#Declaração de classe
from drafts.functionMessages import title


class Employee:
    def __init__(self, name: str, age: int): # Construtor
        # Atributos
     self.name = name
     self.age = age

# Métodos
    def birthday(self):
        self.age += 1

    def message(self):
        return f"{self.name} é funcionário que tem {self.age} anos."

    def sum(self, a: int, b: int) -> int:
        print(f'A={a} B={b}')
        return a + b

    def counter(self, *numbers: int):
        size = len(numbers)
        print(f'Recebi os valores {numbers} e são ao todo {size} numeros.')


# Instanciando objeto de uma classe
title('Instância de objeto')
emp1 = Employee('Alessandra fischer', 20)
print(emp1.message())
emp1.birthday()

title('Realizando soma de 4 + 6')
emp2 = Employee('Roberto fischer', 24)
print(emp2.message())
emp2.birthday()
result = emp2.sum(4, 6)
print('O resultado é : ', result)

title('Contatodor empacotando números')
emp3 = Employee('Vanessa Ortha', 22)
print(emp3.message())
emp3.counter(2, 3, 4)
emp3.counter(6, 7, 8, 9, 10)
emp3.counter(11, 12, 13, 14, 15, 16, 17, 18)
