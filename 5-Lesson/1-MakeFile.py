#Выводим данные пользователя в файл
my_file = open('New_text.txt', 'a')
while True:
    cnt = input('Введите данные для файла. Если закончили - повторно нажмите Enter: ')
    if not cnt:
        break
    else:
        cnt = cnt + '\n'
        my_file.write(cnt)
print('Ввод закончен')
my_file.close()