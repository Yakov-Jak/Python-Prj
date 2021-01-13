# Выводим числа из списка
from random import randint

my_list = [randint(0, 500) for el in range(0, 13)]
print(my_list)
print([my_list[el] for el in range(1, 13) if my_list[el] > my_list[el-1]])
