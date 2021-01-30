# работа с комплексными числами
class Compleks:
    def __init__(self, dest, mnim):
        self.dest = dest
        self.mnim = mnim

    def __add__(self, other):
        d = self.dest + other.dest
        m = self.mnim + other.mnim
        return Compleks(d, m)

    def __mul__(self, other):
        d = (self.dest * other.dest) - (self.mnim * other.mnim)
        m = (self.dest * other.mnim) + (self.mnim * other.dest)
        return Compleks(d, m)

    def __str__(self):
        return (f'{self.dest} + {self.mnim}i ')

z1 = Compleks(2, 5)
z2 = Compleks(3, 5)
r1 = z1 + z2
r2 = z1 * z2
print(r1, r2)