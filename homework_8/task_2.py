import requests
import re

response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
content = response.content.decode(encoding=response.encoding)


pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
result = pattern.findall(content)

pattern_1 = re.compile(r'\d{2}[/]\w+[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}\s[+]\d{4}')
result_1 = pattern_1.findall(content)

pattern_2 = re.compile(r"GET")
result_2 = pattern_2.findall(content)

pattern_3 = re.compile(r"/downloads/product_\d{1}")
result_3 = pattern_3.findall(content)

pattern_4 = re.compile(r"(\d{3})\s(\d{1,3})")
result_4 = pattern_4.findall(content)

my_list = []

for elements in result_4:
    for el in elements:
        my_list.append(el)

my_list_1 = [my_list[i] for i in range(1, len(my_list), 2)]

print(*zip(result, result_1, result_2, result_3, my_list, my_list_1))

