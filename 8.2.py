"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Zero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __truediv__(self, other):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return f'Нельзя делить на ноль'

    def __str__(self):
        return f'{self.__truediv__}'

numbers = Zero((input('Введите цифру 0: ')), (input('Введите цифру 1: ')))

print(numbers[0] / numbers[1])
