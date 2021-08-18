example = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
example_2 = []


for el in example:
    if el.isdigit():
        example_2.append('"')
        if int(el) < 10:
            el = f"0{el}"
            example_2.append(el)
        else:
            example_2.append(el)
        example_2.append('"')

    else:
        if "+" in el:
            example_2.append('"')
            if int(el) < 10:
                el = f"+0{int(el)}"
                example_2.append(el)
            else:
                example_2.append(el)
            example_2.append('"')
        elif "-" in el:
            example_2.append('"')
            if int(el) < 10:
                el = f"-0{int(el)}"
                example_2.append(el)
            else:
                example_2.append(el)
            example_2.append('"')
        else:
            example_2.append(el)

print(example)
print(example_2)


message = ""

for i in range(len(example_2) - 1):
    message += example_2[i]
    if example_2[i].isdigit():
        continue
    elif example_2[i + 1].isdigit():
        continue
    elif "+" in example_2[i + 1]:
        continue
    elif ("+" in example_2[i]) and (example_2[i + 1] == '"'):
        continue
    message += " "
message += example_2[-1]
print(message)
