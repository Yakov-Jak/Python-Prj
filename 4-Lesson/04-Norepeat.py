# Выводим неповторяющиеся элементы списка
my_list = list(input('Введите элементы списка через пробел - ').split())
except_list = set([i for x, i in enumerate(my_list) for y, j in enumerate(my_list) if (x != y) and (i == j)])
sort_list = [el for el in my_list if el not in except_list]
print(sort_list)
