import requests
import json

# x = requests.put(url='http://127.0.0.1:8000/items/name=adney&price=10.0&is_offer=True')

# print(x.status_code)
# print(x.text)

item_name='yana'
item_price=15.0
item_is_offer=False

item_id = 1
# with open('database.json') as json_file:
#     json_decoded = json.load(json_file)
# try:
#     values = json_decoded[str(item_id)]
#     print( f"""
#     item_id = {item_id}
#             item_name = {values['item_name']}
#             item_price = {values['item_price']}
#             item_is_offer = {values['item_is_offer']}""")
# except:
#     print( f"Object with id = {item_id} don't exists" )
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

with open('database.json') as json_file:
    json_decoded = json.load(json_file)

try:
    values = json_decoded[str(item_id)]
    html_response = ""

    columns = json_decoded['columns']
    for column in columns:
        html_response += add_tags('th', column)

except:
    pass

print(add_tags('tr', html_response))