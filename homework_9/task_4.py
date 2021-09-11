class Car:
    speed = 120
    color = "Red"
    name = "BMW"
    is_police = True

    def go(self):
        print("Поехала")

    def stop(self):
        print("Остановилась")

    def turn(self, direction="Налево"):
        print(direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(self.speed)


# class SportCar(Car):

class WorkCar(Car):
    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(self.speed)


# class PoliceCar(Car):

car = TownCar(70)
car.go()
car.turn("Направо")
car.stop()
car.show_speed()

car_1 = WorkCar(35)
car_1.show_speed()
