# Рассчитываем зарплату сотрудников
zp = open('3-ZP_roster.txt')
zp_res = zp.readlines()
name_list = []
zp_sum = 0
for i, el in enumerate(zp_res):
    el = list(el.split())
    zp_sotr = int(el[1])
    zp_sum = zp_sum + zp_sotr
    name_list.append(el[0]) if zp_sotr < 20000 else None
zp_mean = zp_sum / (i+1)
print(f'Сотрудники с зарплатой ниже 20 000 - {name_list}')
print(f'Средняя зарплата в компании - {zp_mean}')
zp.close()
