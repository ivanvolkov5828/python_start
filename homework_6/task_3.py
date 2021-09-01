import json
import sys

my_dict = {}
idx_1 = 0
idx_2 = 0
with open('users.csv', 'r', encoding='utf-8') as f:
    with open("hobby.csv", "r", encoding='utf-8') as file_1:
        for line in f:
            idx_1 += 1
            for el in file_1:
                idx_2 += 1
                my_dict.setdefault(f"{line.strip()}", el.strip())
                break
            if idx_1 > idx_2:
                my_dict.setdefault(f"{line.strip()}", None)
            elif idx_1 < idx_2:
                sys.exit("1")

print(my_dict)
my_dict_str = json.dumps(my_dict)
print(type(my_dict_str))

with open('my_dict.json', 'w', encoding='utf-8') as f:
    f.write(my_dict_str)
