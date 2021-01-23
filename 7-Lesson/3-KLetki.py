# Работаем с клетками
class Cell:
    def __init__(self, ncell):
        self.ncell = ncell

    def __add__(self, other):
        res = self.ncell + other.ncell
        return res

    def __sub__(self, other):
        res = self.ncell - other.ncell
        return res if res > 0 else print('Операция невозможна')


    def __mul__(self, other):
        res = self.ncell * other.ncell
        return res

    def __truediv__(self, other):
        res = round(self.ncell / other.ncell)
        return res

    def make_oder(self):
        for i in range(self.ncell // 5):
            print('*****')
        ost = self.ncell % 5
        print('*' * ost)


a = Cell(55)
b = Cell(24)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
b.make_oder()