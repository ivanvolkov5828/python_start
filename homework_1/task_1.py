# введем продолжительность времени в секундах
duration = int(input("Введите продолжительность времени: "))
# составим условия
if duration <= 60:
    print("{} сек".format(duration))
elif duration <= 3600:
    seconds = duration % 60
    minutes = duration // 60
    print("{} мин {} сек".format(minutes, seconds))
elif duration <= 86400:
    hour = duration // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print("{} час {} мин {} сек".format(hour, minutes, seconds))
else:
    day = duration // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 60
    print("{} дн {} час {} мин {} сек".format(day, hour, minutes, seconds))
