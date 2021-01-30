# Формируем корректный список
class List_cor(Exception):

    def __init__(self, txt):
        self.txt = txt

new_data = 1
my_list = []

while True:
    try:
        new_data = input('Введите новый элемент списка: ')
        if new_data == 'stop':
            break
        elif new_data.isdigit():
            my_list.append(int(new_data))
        else:
            raise List_cor('\n-----Ошибка! Нужно вводить только числа-----\n')
    except List_cor as lc:
        print(lc)


print(f'Наш список получился: {my_list}')
