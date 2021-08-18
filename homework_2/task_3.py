my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(my_list)):
    if my_list[i].isdigit():
        my_list.append('"')
        if int(my_list[i]) < 10:
            my_list[i] = f"0{my_list[i]}"
            my_list.append(my_list[i])
        else:
            my_list.append(my_list[i])
        my_list.append('"')
    else:
        if "+" in my_list[i]:
            my_list.append('"')
            if int(my_list[i]) < 10:
                my_list[i] = f"+0{int(my_list[i])}"
                my_list.append(my_list[i])
            else:
                my_list.append(my_list[i])
            my_list.append('"')

        elif "-" in my_list[i]:
            my_list.append('"')
            if int(my_list[i]) < 10:
                el = f"-0{int(my_list[i])}"
                my_list.append(my_list[i])
            else:
                my_list.append(my_list[i])
            my_list.append('"')
        else:
            my_list.append(my_list[i])


idx = 0

while my_list:
    my_list.pop(0)
    idx += 1
    if idx == 10:
        break

print(my_list)

message = ""

for i in range(len(my_list) - 1):
    message += my_list[i]
    if my_list[i].isdigit():
        continue
    elif my_list[i + 1].isdigit():
        continue
    elif "+" in my_list[i + 1]:
        continue
    elif ("+" in my_list[i]) and (my_list[i + 1] == '"'):
        continue
    message += " "
message += my_list[-1]
print(message)
