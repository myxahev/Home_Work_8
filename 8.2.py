"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Zero:
    def __init__(self, num):
        self.num = int(num)

    def __truediv__(self, other):
        try:
            return self.num / other.num
        except ZeroDivisionError:
            return f'Нельзя делить на ноль'

    def __str__(self):
        return f'{self.__truediv__}'

num_1 = Zero(input('Введите цифру 0: '))
num_2 = Zero(input('Введите цифру 1: '))

print(num_1 / num_2)
