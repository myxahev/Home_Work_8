"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'z = {(self.a * self.b) - (other.b * other.a)} + {(other.a * self.b) + (self.a * other.b) }i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


num1 = ComplexNumber(1, -2)
num2 = ComplexNumber(3, 2)
print(num1)
print(num2)
print(num1 + num2)
print(num1 * num2)