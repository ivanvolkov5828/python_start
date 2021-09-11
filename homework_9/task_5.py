class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки\n")


class Pen(Stationery):
    def __init__(self):
        self.title = "Pen"

    def draw(self):
        print(self.title)
        print("Запуск отрисовки ручкой \n")


class Pencil(Stationery):
    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        print(self.title)
        print("Запуск отрисовки карандашом \n")


class Handle(Stationery):
    def __init__(self):
        self.title = "Handle"

    def draw(self):
        print(self.title)
        print("Запуск отрисовки маркером \n")


stationery = Stationery()
stationery.draw()

first = Pen()
first.draw()

second = Pencil()
second.draw()

third = Handle()
third.draw()