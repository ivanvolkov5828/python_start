def num_translate_adv(number):
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

    if number[0].isupper():
        for key in numbers.keys():
            if number[1:] == key[1:]:
                return numbers[key].title()
    elif numbers.get(f"{number}") is None:
        return None
    else:
        return numbers[f"{number}"]


digit = input("Введите число в виде строки от 1 до 10 на английском языке: ")
print(num_translate_adv(digit))
