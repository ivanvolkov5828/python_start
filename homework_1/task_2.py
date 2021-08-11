# создадим пустой список
numbers = []
# создадим список состоящий из кубов нечетных чисел
for i in range(1, 1001):
    if i % 2 != 0:
        number = i ** 3
        numbers.append(number)
print("Список кубов нечетных чисел")
print(numbers)

# или же можно сделать так
# for i in range(1, 1001, 2):
#     number = i ** 3
#     numbers.append(number)
#
# print(numbers)

# надо вычислить сумму чисел, сумма цифр которого делится нацело на 7

new_numbers = []
sum_1 = 0
for number in numbers:
    if number == 1:
        new_numbers.append(number)
    else:
        while number // 10 != 0:
            remains = number % 10
            sum_1 += remains
            number //= 10

        sum_1 += number
        new_numbers.append(sum_1)
        sum_1 = 0
print("Список, в котором просуммировали цифры чисел предыдущего списка")
print(new_numbers)

sum_2 = 0
for new_number in new_numbers:
    if new_number % 7 == 0:
        sum_2 += new_number

print("Искомая сумая: {}".format(sum_2))

# поменяли список(прибавили ко всем эементам 17)


for i in range(len(numbers)):
    numbers[i] += 17
print("Изначальный список, к каждому элементу которого прибавили 17")
print(numbers)

new_numbers_2 = []
sum_3 = 0
for number in numbers:

    while number // 10 != 0:
        remains = number % 10
        sum_3 += remains
        number //= 10

    sum_3 += number
    new_numbers_2.append(sum_3)
    sum_3 = 0

print("Список, в котором просуммировали цифры чисел предыдущего списка")
print(new_numbers_2)

sum_4 = 0
for new_number_2 in new_numbers_2:
    if new_number_2 % 7 == 0:
        sum_4 += new_number_2

print("снова искомая сумма: {}".format(sum_4))

# задача под звездочкой
# список в котором прибавили ко всем элементам 17 уже есть . Тот же самый список что и в начале, только измененный.
# значит новый не создавал. идем дальше
# тот же самый принцип
# создадим переменную чтобы суммировать
sum_c = 0
sum_5 = 0
for number in numbers:

    while number // 10 != 0:
        remains = number % 10
        sum_c += remains
        number //= 10

    sum_c += number
    if sum_c % 7 == 0:
        sum_5 += sum_c
    sum_c = 0
print("Искомая сумма, только без списка: ", sum_5)