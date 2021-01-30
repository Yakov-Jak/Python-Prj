# Создаем склады с оргтехникой
class Store:

    def __init__(self, mest, stat, v_nabora):
        self.mest = mest
        self.stat = stat
        self.v_nabora = v_nabora
        self.wrhs = {}
        self.items = 0

    def in_store(self, hra_obj):
        self.items += 1
        if self.items <= self.mest:
            self.wrhs[self.items] = hra_obj
        else:
            self.items -= 1
            print('Место на складе закончилось')

    def out_store(self):
        self.items -= 1
        if self.items >= 0:
            self.wrhs.popitem()
        else:
            self.items = 0
            print('Склад пустой')


class Techno:

    def __init__(self, mass, gabarit, data):
        self.mass = mass
        self.gabarit = gabarit
        self.data = data


class Printer(Techno):

    def __init__(self, mass, gabarit, data, v_pech):
        Techno.__init__(self, mass, gabarit, data)
        self.v_pech = v_pech


class Pc(Techno):

    def __init__(self, mass, gabarit, data, pamyat):
        Techno.__init__(self, mass, gabarit, data)
        self.pamyat = pamyat


class Kolonki(Techno):

    def __init__(self, mass, gabarit, data, loudness):
        Techno.__init__(self, mass, gabarit, data)
        self.loudness = loudness


class Otdel:
    def __init__(self):
        self.o_tech = {}
        self.o_item = 0

    def priem(self, sklad, n_poz):
        a = sklad.wrhs.pop(n_poz)
        self.o_tech[self.o_item] = a
        self.o_item += 1
        print(self.o_tech)


class cor_poz(Exception):

    def __init__(self, txt):
        self.txt = txt


sklad_1 = Store(5, 3, 5)
pri = Printer(5, 100, '30-01-2021', 70)
comp1 = Pc(5, 100, '12-01-2021', 1024)
comp2 = Pc(5, 100, '23-01-2021', 2048)
comp3 = Pc(5, 100, '24-01-2021', 8182)
muz1 = Kolonki(5, 100, '17-12-2020', 55)
mux2 = Kolonki(5, 100, '22-01-2021', 60)
ceh = Otdel()
sklad_1.in_store(pri)
sklad_1.in_store(comp1)
sklad_1.in_store(comp2)
sklad_1.in_store(muz1)
print(sklad_1.wrhs)

while True:
    try:
        poz = input(f'Введите номер позиции склада от 0 до {sklad_1.items} для передачи в отдел - ')
        if poz.isdigit():
            poz = int(poz)
            break
        else:
            raise cor_poz('\n-----Ошибка! Позиция склада это целое число-----\n')
    except cor_poz as cp:
        print(cp)

ceh.priem(sklad_1, poz)
print(sklad_1.wrhs)
