# Возводим числа в степень
def stepen(x, y):
    i = 1
    result = x
    if y < 0:
        y = abs(y)
        while i < y:
            result = result * x
            i += 1
        result = 1 / result
    elif y == 0:
        result = 0
    elif y == 1:
        result = x
    else:
        while i < y:
            result = result * x
            i += 1
    return (result)

a = float(input('Введите действиельное число - '))
b = int(input('Введите целое отрицательное число - '))

c = stepen(a, b)
d = a ** b
print(f'{c} - Моя функция\n{d} - Встроенная функция')

