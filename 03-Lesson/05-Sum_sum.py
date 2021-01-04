# Суммируем кучу чисел
def summator(num, nu):
    summa = nu
    num = list((num.title()).split())
    for i in num:
        if i.isdigit():
            summa = summa + int(i)
        elif i == 'Стоп':
            return summa, 'Stop'
        else:
            return summa, 'Continue'
    return summa, 'Continue'


nach_usl = 0
while True:
    numbers = input('Введите числа через пробел или "Стоп" для окончания: ')
    res = summator(numbers, nach_usl)
    print(f'Сумма чисел - {res[0]}')
    if res[1] == 'Stop':
        break
    else:
        nach_usl = res[0]
