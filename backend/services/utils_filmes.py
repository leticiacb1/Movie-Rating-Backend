import os
import json
from dotenv import load_dotenv

load_dotenv()
DB_FILMS_ID = os.getenv('DB_FILMS_PATH')

def create_film(new_data):
    try:
        # 1. Read file contents
        with open(DB_FILMS_ID) as file:
            data = json.load(file)

        # 2. Update json object
        data.append(new_data.dict())

        # 3. Write json file
        with open(DB_FILMS_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")


def get_film():

    # 1. Read file contents
    with open(DB_FILMS_ID, "r") as file:
        data = json.load(file)

    return data