def main(argv):
    program, *args = argv
    my_list = []
    my_list_1 = []

    if len(args) == 0:
        with open("bakery.csv", "r+", encoding="utf-8") as f:
            print(f.read())
    elif args[0] and len(args) == 1:
        with open("bakery.csv", "r+", encoding="utf-8") as f:
            for line in f:
                my_list.append(line.strip())
        idx = int(args[0])
        print(" ".join(my_list[idx:]))
    if len(args) > 1:
        with open("bakery.csv", "r+", encoding="utf-8") as f:
            for line in f:
                my_list_1.append(line.strip())
        idx_2 = int(args[0])
        idx_1 = int(args[1])
        print(" ".join(my_list_1[idx_2:idx_1 + 1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)
