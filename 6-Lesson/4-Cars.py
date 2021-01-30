# Собираем гараж
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.velocity = 0

    def go(self):
        self.velocity = self.speed
        print(f'Машина поехала.')

    def stop(self):
        self.velocity = 0
        print('Машина остановилась')


    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость авто - {self.velocity}км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, fuel):
        Car.__init__(self, speed, color, name, is_police)
        self.fuel = fuel

    def show_speed(self):
        print('Превышение скорости!') if self.speed > 60 else print(f'Текущая скорость авто - {self.speed}км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, price):
        Car.__init__(self, speed, color, name, is_police)
        self.price = price

    def nalog(self):
        tax = self.price * 0.02
        print(f'Налог на спортивную машину составит {tax}$')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, typ):
        Car.__init__(self, speed, color, name, is_police)
        self.typ = typ

    def show_speed(self):
        print('Превышение скорости!') if self.speed > 40 else print(f'Текущая скорость авто - {self.speed}км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, rang):
        Car.__init__(self, speed, color, name, is_police)
        self.rang = rang

    def shtraf(self):
        print(f'Штраф будет 1000$') if self.rang == 'polkovnik' else print(f'Штраф будет 100$')


lada = Car(180, 'Вишнёвый', 'Девятка', False)
lada.turn('направо')

volvo = TownCar(100, 'Синий', 'Ласточка', False, 'Дизель')
volvo.go()
volvo.show_speed()
volvo.speed = 55
volvo.show_speed()

plk = PoliceCar(200, 'Черный', 'Полкан', True, 'polkovnik')
plk.shtraf()
plk.rang = 'kapitan'
plk.shtraf()


