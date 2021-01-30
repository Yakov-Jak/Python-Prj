# Формируем исключение при делении на ноль
class My_except(Exception):

    def __init__(self, mes):
        self.mes = mes

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if b == 0:
        raise My_except('Нельзя делить на ноль')
    else:
        print(a / b)
except My_except as mex:
    print(mex)
else:
    print('Все прошло успешно')

