# Создаём классы работников
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def info(self):
        print(self.name)
        print(self.surname)
        print(self.position)
        print(self._income)
        print('\n')


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя работника - {self.surname} {self.name}\n')

    def get_total_income(self):
        tot_inc = self._income['wage'] + self._income['bonus']
        print(f'Полный доход сотрудника равен {tot_inc}$\n')


maxs = Worker('Максим', 'Сидоров', 'Сварщик', 50000, 22000)
luba = Position('Люба', 'Иванова', 'Оператор крана', 30000, 15000)
luba.info()
luba.get_full_name()
luba.get_total_income()
print(f'Фамилия Максима - {maxs.surname}\n')
print(f'Доходы Макисма: {maxs._income}\n')
