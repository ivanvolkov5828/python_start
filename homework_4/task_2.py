from requests import get


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

    return my_list_2[idx], response.headers["date"]


exchange = input("Введите код валюты: ")
print(currency_rates(exchange))
