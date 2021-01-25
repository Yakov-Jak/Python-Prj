my_file = open('2-Super_text.txt', 'r')
cnt = my_file.readlines()
for i, el in enumerate(cnt):
    q_wrds = (len(list(el.split())))
    print(f'В строке {i+1} слов - {q_wrds}')

print(f'Всего строк в файле: {i+1}')
my_file.close()
