import shutil
import os

dir_name = "my_project_1"
my_path_1 = r"C:\Users\volko\OneDrive\Рабочий стол\python_start\homework_7\my_project_1\- authapp\templates"
my_path_2 = r"C:\Users\volko\OneDrive\Рабочий стол\python_start\homework_7\my_project_1\- mainapp\templates"

for f in os.listdir(my_path_1):
    if os.path.isfile(os.path.join(my_path_1, f)):
        shutil.copy(os.path.join(my_path_1, f), os.path.join(my_path_2, f))
    if os.path.isdir(os.path.join(my_path_1, f)):
        os.system(f'rd /S /Q {my_path_2}\\{f}')
        try:
            shutil.copytree(os.path.join(my_path_1, f), os.path.join(my_path_2, f))
        except Exception as e:
            print(f"Ой, файл уже создан {e}")
