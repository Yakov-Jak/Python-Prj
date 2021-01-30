# Создаём канцелярские принадлежности
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Напишем ручкой {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Нарисуем карандашом {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Выделим маркером {self.title}')


dog = Stationery('Собака')
dog.draw()

cat = Pen('Кошка')
cat.draw()

mouse = Pencil('Мышь')
mouse.draw()

bird = Handle('Птичка')
bird.draw()
