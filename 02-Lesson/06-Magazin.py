# Формируем базу данных
menu = '1 - Ввести характеристики (текущие данные о товарах будут потеряны)\n' \
       '2 - Отобразить характеристики\n' \
       '3 - Ввести данные товара\n' \
       '4 - Посмотреть состояние склада\n' \
       '5 - Отобразить аналитику по товарам\n' \
       '6 - Выход'
# Пришлось заранее задать несколько пустых словарей. По другому пока не получилось
# Вынужденное ограничение емкости склада
tov1 = {}
tov2 = {}
tov3 = {}
tov4 = {}
tov5 = {}
tov6 = {}
tov7 = {}
tov8 = {}
tov9 = {}
tov10 = {}
tovar_opis = {}  # Далее в коде закоментированы строки, с которыми не получилось
tovar_op = [tov1, tov2, tov3, tov4, tov5, tov6, tov7, tov8, tov9, tov10]
tovar = ()
sklad = []
analitics = []
analit = {}
types = []
t = 1
k = 0
while True:
    print(menu)
    vib_men = input('Выберите пункт меню - ')

    if vib_men == '1':
        analitics = (input('Введите характеристики для формирования склада - ').title()).split()
        t = 1
        k = 0

    elif vib_men == '2':
        print(f'Анализируем товары по следующим параметрам:\n {analitics}')

    elif vib_men == '3':
        print('Ввод информации о товаре')
        for item in analitics:
            temp = input(f'Введите {item} - ')
            temp = int(temp) if temp.isdigit() else temp
            # tovar_opis[item] = temp - Не получается корректно сделать базу, если использовать временный словарь.
            tovar_op[k][item] = temp

        # tovar = (t, tovar_opis) При добавлении последующего словаря в корте в старом значения словаря также меняются
        tovar = (t, tovar_op[k])
        types.append(k)
        types[k] = []
        t += 1
        k += 1

        print(f'Внесли в базу информацию о товаре:\n{tovar}')
        sklad.append(tovar)  # Если заранее не создать пустые словари, то в базе все значения
        # меняются на значения последнего введенного товара

    elif vib_men == '4':
        print('Вот такой у нас склад:')
        for ind in range(0, len(sklad)):
            print(sklad[ind])

    elif vib_men == '5':
        print(f'Вот такой у нас склад:')
        for ind, item in enumerate(analitics):
            for ind1 in range(0, len(sklad)):
                types[ind].append(tovar_op[ind1][item])
            analit[item] = list(set(types[ind]))
            print(f'{item}: {analit.get(item)}')

    elif vib_men == '6':
        break

    else:
        print('Повторите ввод')
