class OwnError(ValueError):
    def __init__(self, txt):
        self.txt = txt


def list_gen(argv):
    program, *args = argv
    my_list = []

    while True:

        try:
            try:

                el = int(input("Введите пожалуйста элемент: "))

                if el == 666:
                    break

                my_list.append(el)

            except OwnError(ValueError) as e:
                print(e)

        except TypeError as e:
            print(e)

    print(my_list)


if __name__ == '__main__':
    import sys
    list_gen(sys.argv)
