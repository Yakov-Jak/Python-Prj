# Запускаем скрипт с параметрами
from sys import argv

script_name, work_hours, rate, bonus = argv

zp = int(work_hours)*int(rate)+int(bonus)
print(f'Зарплата равна - {zp}')
