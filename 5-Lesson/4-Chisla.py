# Заменяем язык чисел
eng_num = open('4-Numbers.txt', 'r')
rus_num = open('4-Rus_numbers.txt', 'a')
dict_num = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
eng_num_cnt = eng_num.readlines()

for el in eng_num_cnt:
    eng_dict = list(el.split())
    eng_dict[0] = dict_num.get(eng_dict[2])
    rus_dict = ' '.join(eng_dict) + '\n'
    rus_num.write(rus_dict)

eng_num.close()
rus_num.close()
