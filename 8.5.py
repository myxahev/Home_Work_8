"""
Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""

class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, name, make, year, series):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.make} {self.year} {self.series}'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year, ip=None):
        super().__init__(name, make, year)
        self.ip = ip

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year, model=None):
        super().__init__(name, make, year)
        self.model = model

    def action(self):
        return 'Копирует'


warehouse = Warehouse()
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90)
warehouse.add_to(scaner)
scaner = Scaner('hp', '311', 97)
warehouse.add_to(scaner)
xerox = Xerox('hp', '330', 99)
warehouse.add_to(xerox)
printer = Printer('sony', 126, 2018, 'e-320')
warehouse.add_to(printer)
# выводим склад
print(warehouse._dict)
warehouse.extract('Scaner')
print()
print(warehouse._dict)