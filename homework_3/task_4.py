def thesaurus_adv(*args):
    my_list = list(args)
    new_list = my_list.copy()
    help_list = []
    help_list_1 = []
    dict_name = {}
    dict_name_1 = {}
    dict_name_2 = {}
    dict_name_3 = {}

    for element in my_list:
        filter_list = filter(lambda el: el.startswith(f'{element[0]}'), my_list)
        my_list_3 = list(filter_list)
        dict_name.setdefault(f'{element[0]}', my_list_3)
        filter_list = []
    print(dict_name)
    print(new_list)

    for key, value in dict_name.items():
        for element in value:
            name_1 = element.split()[-1][0]
            name_1_1 = element[0]
            for el in new_list:
                name = el.split()[-1][0]
                name_el = el[0]
                if name_1_1 != name_el and name_1 == name:
                    help_list_1.append(el)
                    dict_name_3.setdefault(f"{name_el}", help_list_1)
                elif name_1 == name:
                    help_list.append(el)

            dict_name_1.setdefault(f"{key}", help_list)
            dict_name_1.update(dict_name_3)
            dict_name_2.setdefault(element.split()[-1][0], dict_name_1)
            help_list = []
            help_list_1 = []
            dict_name_1 = {}
            dict_name_3 = {}
    print(dict_name_2)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# переписать условие потому что находит Илья Иванов Илья Иванов и добавляет в список
