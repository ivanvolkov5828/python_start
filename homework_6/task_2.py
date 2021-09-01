from collections import Counter
import json

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    nums = json.load(f)

new_list = []

for el in nums:
    new_list.append(tuple(el))


def most_frequent(num):
    count_2 = Counter(num)

    return count_2.most_common(1)[0][0]


print(f"IP адрес спамера:  {most_frequent(new_list)[0]}")
print(f"Количество отправленных им запросов: {new_list.count(most_frequent(new_list))}")
