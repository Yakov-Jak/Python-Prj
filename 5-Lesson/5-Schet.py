#Считаем числа в файле
from functools import reduce


def summs(a, b):
    a = int(a)
    b = int(b)
    return a + b


with open("5-schet.txt", "w") as sch:
    cnt = input('Введите числа через проблел: ')
    sch.write(cnt)

with open("5-schet.txt", "r") as sch:
    cnt = sch.read()
    cnt = list(cnt.split())
    result = reduce(summs, cnt)
    print(f'Сумма чисел в файле равна = {result}')
