import os
from os.path import relpath
import django


def main(argv):
    program, *args = argv

    my_dict = {}
    my_list = [100, 1000, 10000, 100000]

    list_21 = []

    root_dir = django.__path__[0]

    for el in my_list:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                rel_path = relpath(os.path.join(root, file), root_dir)
                if os.stat(os.path.join(root_dir, rel_path)).st_size < el:
                    list_21.append(rel_path)

        my_dict.setdefault(el, len(list_21))
        list_21 = []
    print(my_dict)


if __name__ == '__main__':
    import sys
    main(sys.argv)
