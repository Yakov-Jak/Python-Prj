#Определяем тип данных в списке
note = ['Петя', 'Rock', 12, 13, 1.5, False, 98, True, 8.0]
k = len(note)
i = 0

while i < k:
    print(type(note[i]))
    i += 1

print (f'The end. There are {k} items')
