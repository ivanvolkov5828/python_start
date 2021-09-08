import re


def email_parse(email_address):
    my_dict = {}

    pattern_1 = re.compile(r'^(\w+[A-za-z/.-]\w+)')
    pattern_2 = re.compile(r'(\w+\.\w+)$')

    my_dict['username'] = ''.join(pattern_1.findall(email_address))
    my_dict['domain'] = ''.join(pattern_2.findall(email_address))

    return my_dict


print(email_parse("someone@geekbrains.ru"))
