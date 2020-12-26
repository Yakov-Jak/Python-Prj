# Определяем самое большую цифру в числе
num = input('Введите число:')
n_sym = len(num)
k = 0
i = 9
while i != 0:
    while k < n_sym:
        temp = int(num[k])
        if temp == i:
            print('Самая большая цифра -', temp)
            jum = i
            i = 1
            break
        else:
            k = k + 1
            jum = 0
    i = i - 1
    k = 0
if jum > 0:
    print('Разобрались!')
else:
    print('Цифр нет')


