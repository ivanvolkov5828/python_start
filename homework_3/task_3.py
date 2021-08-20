def thesaurus(*args):
    my_list = list(args)
    dict_name = {}

    for element in my_list:
        filter_list = filter(lambda el: el.startswith(f'{element[0]}'), my_list)
        my_list_3 = list(filter_list)
        dict_name.setdefault(f'{element[0]}', my_list_3)
        filter_list = []
    return dict_name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
