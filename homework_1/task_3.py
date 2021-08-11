idx = 0
while idx < 100:
    idx += 1
    if idx == 1:
        print(idx, "Процент")
    elif (idx > 4) and (idx <= 20):
        print(idx, "Процентов")
    elif idx % 10 == 1:
        print(idx, "Процент")
    elif idx % 10 == 2 or idx % 10 == 3 or idx % 10 == 4:
        print(idx, "Процента")
    elif idx % 10 == 5 or idx % 10 == 6 or idx % 10 == 7 or idx % 10 == 8 or idx % 10 == 9 or idx % 10 == 0:
        print(idx, "Процентов")
