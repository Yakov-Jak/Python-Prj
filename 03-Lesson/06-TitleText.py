# Делаем большие буквы
# def title_let(words): - простой способ
#     words = words.title()
#     return words

def title_let(word):    # мой способ
    sen_b = bytearray(word.encode('windows-1251'))
    sen_b[0] = sen_b[0] - 32
    return sen_b.decode('windows-1251')


sen = list((input('Введите слова с маленькой буквы - ')).split())
for i, item in enumerate(sen):
    sen[i] = title_let(item)
    print(sen[i])
