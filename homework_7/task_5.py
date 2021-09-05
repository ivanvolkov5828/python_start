import os
from os.path import relpath
import django


def main(argv):
    program, *args = argv

    my_dict = {}
    my_list = [100, 1000, 10000, 100000]

    list_21 = []
    list_31 = []
    list_41 = []

    type_1 = "py"
    type_2 = "html"

    root_dir = django.__path__[0]

    for el in my_list:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                rel_path = relpath(os.path.join(root, file), root_dir)
                ext = file.rsplit('.', maxsplit=1)[-1].lower()
                if os.stat(os.path.join(root_dir, rel_path)).st_size < el:
                    list_21.append(rel_path)
                    list_31.append(ext)

        if type_1 and type_2 in list_31:
            list_41.append(type_1)
            list_41.append(type_2)
            my_dict.setdefault(el, (len(list_21), list_41))
            list_41 = []
        elif type_1 in list_31:
            list_41.append(type_1)
            my_dict.setdefault(el, (len(list_21), list_41))
            list_41 = []
        elif type_2 in list_31:
            list_41.append(type_2)
            my_dict.setdefault(el, (len(list_21), list_41))
            list_41 = []

        list_21 = []
    print(my_dict)


if __name__ == '__main__':
    import sys

    main(sys.argv)
