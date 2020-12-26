# Планируем тренировки
dist_a = float(input('Введите начальную дистанцию бегуна - '))
dist_b = float(input('Введите целевую дистанцию бегуна - '))
i = 1
while dist_b >= dist_a:
    print('{:d}-й день пробежали: {:.2f} км' .format(i,dist_a))
    dist_a = dist_a * 1.1
    i = i + 1
print('{:d}-й день пробежали: {:.2f} км' .format(i,dist_a))
print('Достигли цели на {:d}-й день'.format(i))

