class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

try:

    if second == 0:
        raise OwnError("На ноль делить нельзя!!")
    res = first / second

except OwnError as err:
    print(err)

else:
    print(f"Все хорошо. Результат - {res}")

finally:
    print("Программа завершена")
