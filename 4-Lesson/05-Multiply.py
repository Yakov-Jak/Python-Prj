# Перемножаем все элементы списка
from functools import reduce

gener = [el for el in range(100, 1001, 2)]


def multy(a, b):
    return a * b


print(reduce(multy, gener))
