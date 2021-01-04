# Делим числа
def delitel(k1, k2):
    if k2 == 0:
        print('Нельзя делить на 0')
        result = None
        return result
    else:
        result = k1 / k2
        return result

a = int(input('Введите делимое число - '))
b = int(input('Введите делитель - '))
c = delitel(a, b)
print(f'{c:.2f}')
