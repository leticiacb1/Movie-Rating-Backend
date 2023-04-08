import requests
import json

x = requests.put(url='http://127.0.0.1:8000/items/name=leticia&price=10.0&is_offer=False')

print(x.status_code)
print(x.text)