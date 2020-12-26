# Работаем с часами
sec = int(input("Введите секунды - "))
minut = sec//60
hour = minut//60
sec = sec - minut * 60
minut = minut - hour * 60
print('{}:{}:{}'.format(hour, minut, sec))
