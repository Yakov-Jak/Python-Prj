#Выводим факториал
from functools import reduce


def mul(a, b):
    return a * b


def fact(n):
    for el in range(1, n+1):
        yield reduce(mul, range(1, el+1))


temp = int(input('Введите аргумент факториала - '))
for el in fact(temp):
    print(el)
