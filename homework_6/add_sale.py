def main(argv):
    program, *args = argv
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(f"{args[0]}\n")


if __name__ == '__main__':
    import sys
    main(sys.argv)
