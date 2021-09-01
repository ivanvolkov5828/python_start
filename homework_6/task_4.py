with open('users.csv', 'r', encoding='utf-8') as f:
    with open("hobby.csv", "r", encoding='utf-8') as file_1:
        for line in f:
            for el in file_1:
                users_hobby = f"{line.strip()}: {el.strip()}\n"
                f = open("users_hobby.txt", "a", encoding="utf-8")
                f.write(users_hobby)
                break

