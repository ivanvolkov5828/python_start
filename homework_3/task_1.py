def num_translate(number):
    numbers = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    if numbers.get(f"{number}") is None:
        return None
    else:
        return numbers[f"{number}"]


digit = input("Введите число в виде строки от 1 до 10 на английском языке: ")
print(num_translate(digit))
