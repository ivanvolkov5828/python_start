numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_numbers = set()
repeats = set()

for el in numbers:
    if el not in repeats:
        unique_numbers.add(el)
    else:
        unique_numbers.discard(el)
    repeats.add(el)


unique_numbers_ord = [el for el in numbers if el in unique_numbers]
print(unique_numbers_ord)