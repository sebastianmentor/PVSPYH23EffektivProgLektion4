from dataclasses import dataclass, field
from typing import List
import random

@dataclass
class Human:
    name: str
    age: int
    occupation: str

    def kill_human(self) -> bool:
        if random.randint(0,1):
            del(self)

# class Human:
#     def __init__(self, name:str) -> None:
#         self.name = name 


#     def __repr__(self) -> str:
#         return f"Human({self.name})"
    
#     def __eq__(self, value: object) -> bool:
#         pass

# human1 = Human('Kalle')
# human2 = Human('Kalle')

# if human1 == human2:
#    print(repr(human1))

@dataclass
class Grade:
    subject: str
    grade: int

@dataclass
class Student:
    name: str
    age: int
    grades: List[int] = field(default_factory=list)
    # grades: List[Grade] = field(default_factory=list)
    id: int = field(default=0, compare=False)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


class StupidClass:
    def __init__(self,dum_lista:list=[]) -> None:
        self.lista = dum_lista
    # @property
    # def lista(self):
    #     return self._lista

a = StupidClass()
b = StupidClass()

a.lista.append('42')
print(b.lista)
b.lista.append('OMG!!!')
print(a.lista)
print(b.lista)
print(a.lista is b.lista)

c = StupidClass()
print(c.lista)
print('-'*30)
c.lista = []
print(a.lista)
print(b.lista)
print(c.lista)

# kalle = Student('Kalle', 23, id = 100)
# linda = Student('Linda', 33, id = 101)

# print(repr(kalle))
# print(repr(linda))
# kalle.grades.append(12)
# linda.grades.append(23)
# print(repr(kalle))
# print(repr(linda))
# kalle.grades.append(88)
# linda.grades.append(50)
# print(repr(kalle))
# print(repr(linda))








