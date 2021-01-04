# Суммируем два самых больших числа
def my_func(a1, a2, a3):
    num = [a1, a2, a3]
    num.sort(reverse=True)
    summ = num[0]+num[1]
    print(summ)


cifr = input('Введите числа через пробел - ').split()
for i, item in enumerate(cifr):
    cifr[i] = int(item)

my_func(cifr[0], cifr[1], cifr[2])
