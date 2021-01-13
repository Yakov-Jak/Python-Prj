# Скрипт итераторов
from sys import argv
from itertools import count, cycle

# Работа итератора count()
script_name, start = argv
start = int(start)

for el in count(start):
    if el > 22:
        break
    else:
        print(el)

# -------------------------------------------------------------------

# Работа итератора cycle()
# script_name, stop = argv
# stop = int(stop)
# reset = 0
# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December')
#
# for el in cycle(months):
#     if reset > stop:
#         break
#     else:
#         print(el)
#         reset += 1

