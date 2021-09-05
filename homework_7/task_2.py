import json
import os

with open("config.yaml", "r", encoding="utf-8") as f:
    for line in f:
        for el in line.split(":"):

            if el == "my_project":
                dir_name = el
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)

            my_set = ("- settings", "- mainapp", "- authapp")
            my_set_1 = ("- mainapp", "- authapp")

            if "__init__.py" in line:
                for directory in my_set:
                    my_path = os.path.join(dir_name, directory)
                    if not os.path.exists(my_path):
                        os.makedirs(os.path.join(dir_name, directory))

                        file_path = os.path.join(my_path, "__init__.py")
                        with open(file_path, 'w') as file:
                            file.write("этот текст создан автоматически")

            if "models.py" in line:
                for directory in my_set_1:
                    my_path = os.path.join(dir_name, directory)
                    if os.path.exists(my_path):
                        file_path = os.path.join(my_path, "models.py")
                        with open(file_path, 'w') as file:
                            file.write("этот текст создан автоматически")

            if "views.py" in line:
                for directory in my_set_1:
                    my_path = os.path.join(dir_name, directory)
                    if os.path.exists(my_path):
                        file_path = os.path.join(my_path, "views.py")
                        with open(file_path, 'w') as file:
                            file.write("этот текст создан автоматически")

            if "dev.py" in line:
                my_path = os.path.join(dir_name, "- settings")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "dev.py")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")

            if "prod.py" in line:
                my_path = os.path.join(dir_name, "- settings")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "prod.py")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")

            if "templates" in line:
                for directory in my_set_1:
                    my_path = os.path.join(dir_name, directory, "templates")
                    if not os.path.exists(my_path):
                        os.makedirs(os.path.join(dir_name, directory, "templates"))

            if "mainapp" in line:
                my_path = os.path.join(dir_name, "- mainapp", "templates", "mainapp")
                if not os.path.exists(my_path):
                    os.makedirs(os.path.join(dir_name, "- mainapp", "templates", "mainapp"))

            if "authapp" in line:
                my_path = os.path.join(dir_name, "- authapp", "templates", "authapp")
                if not os.path.exists(my_path):
                    os.makedirs(os.path.join(dir_name, "- authapp", "templates", "authapp"))

            if "base.html" in line:

                my_path = os.path.join(dir_name, "- mainapp", "templates", "mainapp")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "base.html")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")

                my_path = os.path.join(dir_name, "- authapp", "templates", "authapp")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "base.html")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")

            if "index.html" in line:
                my_path = os.path.join(dir_name, "- mainapp", "templates", "mainapp")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "index.html")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")

                my_path = os.path.join(dir_name, "- authapp", "templates", "authapp")
                if os.path.exists(my_path):
                    file_path = os.path.join(my_path, "index.html")
                    with open(file_path, 'w') as file:
                        file.write("этот текст создан автоматически")


