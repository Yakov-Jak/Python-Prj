# Вводим информацию о пользователях
users_que = ('Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'E-mail', 'Телефон')
users_data = []

for item in users_que:
    temp = input(f'Введите {item} - ')
    users_data.append(temp)

def func(sec_name, name, cell, email, year, cit):
    print(f'{sec_name} {name} живет в {cit}, родился в {year} году. Можно позвонить {cell} или написать {email}')

func(name=users_data[0], sec_name=users_data[1], year=users_data[2], cit=users_data[3], email=users_data[4],
     cell=users_data[5])
