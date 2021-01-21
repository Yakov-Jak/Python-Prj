# Считаем массу асфальта
class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        l = self._lenght
        w = self._width
        mass_per_qm = 30
        t = 4
        mass = l * w * mass_per_qm * t / 1000
        print(f'Масса асфальтового покрытия дороги - {mass} тонн')

r1 = Road(10000, 20)
r1.calc()