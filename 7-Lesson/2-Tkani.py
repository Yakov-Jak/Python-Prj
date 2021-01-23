# Рассчет ткани
from abc import ABC, abstractmethod

class Wear(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def clcalc(self):
        pass

class Coat(Wear):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def clcalc(self):
        c = round((self.size / 6.5 + 0.5), 2)
        return c


class Suit(Wear):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def clcalc(self):
        c = round((self.size * 2 + 0.3), 2)
        return c


my_suit = Suit(13)
my_coat = Coat(180)
print(my_coat.clcalc)
print(my_suit.clcalc)
