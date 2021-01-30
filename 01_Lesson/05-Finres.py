# Считаем финансовые показатели
val = int(input("Введите размер выручки - "))
exp = int(input('Размер издержек в компании - '))
if val >= exp:
    profit = val - exp
    rent = profit / val * 100
    print('Ура! Заработали прибыль\nРентабельность составила - {:.1f} %' .format(rent))
    pers = int(input('Введите количество персонала - '))
    eff = profit / pers
    print('Прибыль на одного сотрудника составит - {:.1f} целковых' .format(eff))
else:
    print('Убыток((( Будем работать лучше!')

