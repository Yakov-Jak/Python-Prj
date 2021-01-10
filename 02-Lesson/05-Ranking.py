# Ранжируем слова
rnk = [7, 5, 3, 3, 2]
var = int(input('Введите натуральное число - '))
i = 0
while i < len(rnk):
    if var > rnk[i]:
        rnk.insert(i, var)
        break
    else:
        i += 1

print(rnk)