def main(argv):
    program, *args = argv
    with open(f'{args[0]}', 'r', encoding='utf-8') as f:
        with open(f"{args[1]}", "r", encoding='utf-8') as file_1:
            for line in f:
                for el in file_1:
                    users_hobby = f"{line.strip()}: {el.strip()}\n"
                    f = open(f"{args[2]}", "a", encoding="utf-8")
                    f.write(users_hobby)
                    break
    return 0


if __name__ == '__main__':
    import sys
    main(sys.argv)
