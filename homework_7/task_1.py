import os


def main():
    # program, *args = argv
    dir_name = 'my_project'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    my_dirs = ("settings", "mainapp", "adminapp", "authapp")
    for el in my_dirs:
        if not (el in dir_name):
            try:
                os.makedirs(os.path.join(dir_name, el))
            except Exception as e:
                print(f'Такая папка уже создана, поэтому выдает ошибку: {e}')


if __name__ == '__main__':
    # main(sys.argv)
    main()
