import os
import json
from dotenv import load_dotenv

load_dotenv()
DB_AVALIACAO_ID = os.getenv('DB_RATING_PATH')

def create_rating(new_data):
    try:
        # 1. Read file contents
        with open(DB_AVALIACAO_ID) as file:
            data = json.load(file)

        # 2. Update json object
        data.append(new_data.dict())

        # 3. Write json file
        with open(DB_AVALIACAO_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def update_rating(id : int , new_data : dict):
    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        for item in data:
            if(item['id'] == id):

                item['comment'] = new_data['comment']
                item['score'] = new_data['score']
                break
        
        # 3. Write json file
        with open(DB_AVALIACAO_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def delete_rating(id:int):

    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        for idx, item in enumerate(data):
            if(item['id'] == id):
                data.pop(idx)
                
        # 3. Write json file
        with open(DB_AVALIACAO_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def get_rating(id):

    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        result = ""
        for item in data:
            if(item['id'] == id):
                result = item

    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return result

def get_all_rating():

    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return data