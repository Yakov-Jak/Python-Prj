# Разделяем слова
words = (input('Введите слова какие нравятся - ').title()).split()
# words = words.split()

# Ручной вариант
i = 1
while i < (len(words) + 1):
    print(f"{i}. {words[i-1][:10]}")
    i += 1

# Вариант через enumerate
# for ind, el in enumerate(words):
#     print (ind, el[:10])
