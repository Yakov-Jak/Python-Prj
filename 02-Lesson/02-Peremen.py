# Меняем местами числа
print("Вводите данные для списка пока не надоест.\nДля завершения ввода впишите 'Хватит'")
tok = []
insert = input()
while insert != 'Хватит':
     tok.append(insert)
     insert = input()

print(tok)
kot = tok[::2]
temp = tok[1::2]
lnt = len(temp)
count = 0

while count < lnt:
    kot.insert(count*2,temp[count])
    count += 1

print(kot)
