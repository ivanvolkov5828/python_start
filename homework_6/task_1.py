import requests
import json

response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
content = response.content.decode(encoding=response.encoding)

request_type = []
requested_resource = []
remote_addr = []

for el in content.split('] "')[1:]:
    request_type.append(el.split(" /")[0])

for el in content.split("GET ")[1:]:
    requested_resource.append(el.split(" HTTP")[0])

for el in content.split("\n"):
    remote_addr.append(el.split(" - - ")[0])

result = list(zip(remote_addr, request_type, requested_resource))
print(result)

with open('nginx_logs.txt', 'w', encoding="utf-8") as f:
    json.dump(result, f)

# with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
#     f.write(f"{result}")
