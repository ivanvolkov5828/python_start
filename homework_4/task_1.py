from requests import get
from decimal import *


def currency_rates(currency):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.content.decode(encoding=response.encoding)

    my_list = []
    my_list_2 = []
    idx = 0

    for el in content.split("<CharCode>")[1:]:
        my_list.append(el.split("</CharCode>")[0])

    for el in content.split("<Value>")[1:]:
        my_list_2.append(el.split("</Value>")[0])

    for el in my_list:
        if el == currency:
            idx = my_list.index(el)

    #print(my_list_2)
    #answer = tuple(map(float, my_list_2))
    #print(answer)
    return my_list_2[idx]


exchange = input("Введите код валюты: ")
print(currency_rates(exchange))
