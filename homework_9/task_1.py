import time


class TrafficLight:
    __color = 0

    def __init__(self, red, yellow, green):
        self.__color = red
        self.yellow = yellow
        self.green = green

    def running(self):
        if self.__color == "Red":
            print(self.__color, end="")
            time.sleep(7)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть красный цвет")

        if self.yellow == "Yellow":
            print(self.yellow, end="")
            time.sleep(2)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть желтый цвет")

        if self.green == "Green":
            print(self.green, end="")
            time.sleep(3)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть зеленый цвет")


light = TrafficLight("Red", "Yellow", "Green")
light.running()
