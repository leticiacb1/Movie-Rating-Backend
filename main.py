from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import json

app = FastAPI()

#TORUN: uvicorn main:app --reload
#  http://127.0.0.1:8000/items/


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return "Hello World"

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, q: Union[str, None] = None):
    
    with open('database.json') as json_file:
        json_decoded = json.load(json_file)

    try:
        data = json_decoded[str(item_id)]
        columns = json_decoded['columns']

        # adding columns to html response
        html_columns = ""
        for column in columns:
            html_columns += add_tags('th', column)
        html_columns = add_tags('tr', html_columns)

        # adding alues to html response
        html_values = add_tags("td", str(item_id))
        for value in data.values():
            html_values += add_tags('td', value)
        html_values = add_tags('tr', html_values)

        return "<style>table, th, td {border:1px solid black;}</style>" + add_tags('table', html_columns + html_values)
    except:
        return f"Object with id = '{item_id}' don't exists"


@app.put("/items/name={item_name}&price={item_price}&is_offer={item_is_offer}")
def create_item(item_name: str, item_price: float, item_is_offer: bool):

    data = {
    'item_name': item_name,
    'item_price': item_price, 
    'item_is_offer': item_is_offer
    }
    json_file = 'database.json'



    with open(json_file) as json_file:
        json_decoded = json.load(json_file)

    item_id = json_decoded['id'] + 1

    for i in range(1, item_id):
        if item_name == json_decoded[str(i)]["item_name"]:
            return f"Object with name = '{item_name}' already exists"
        
    json_decoded['id'] += 1

    json_decoded[item_id] = data

    with open('database.json', 'w') as json_file:
        json.dump(json_decoded, json_file)
    
    return "Item created successfully!"
