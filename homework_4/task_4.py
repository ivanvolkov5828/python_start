from requests import get
import sys


def currency_rates(argv):
    program, *args = argv
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
        if el == argv:
            idx = my_list.index(el)

    return my_list_2[idx], response.headers["date"]


if __name__ == '__main__':
    print(currency_rates("EUR"))
    print(currency_rates("USD"))
