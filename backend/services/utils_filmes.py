import os
import json
from dotenv import load_dotenv

load_dotenv()
DB_FILMS_ID = os.getenv('DB_FILMS_PATH')

def create_film(new_data):
    try:
        # 1. Read 
        with open(DB_FILMS_ID) as file:
            data = json.load(file)

        # Verifica se o objeto ja esta cadastrado:
        dict_data = new_data.dict()
        for film_id, item in data.items():
            if(film_id.isdigit()):
                if(item["name"] == dict_data["name"] and item["description"] == dict_data["description"] 
                    and item["release_year"] == dict_data["release_year"] and item["length"] == dict_data["length"]):

                    return "Filme já cadastrado"
        
        # 2. Update json 
        film_id = int(data['count_id']) + 1
        data.update({ str(film_id): dict_data})
        
        # Atualiza controle de count_id:
        data['count_id'] = film_id
        
        # 3. Write 
        with open(DB_FILMS_ID, "w") as file:
            json.dump(data, file , indent=2)

        return "OK" 
    except Exception as e:
        print(f" [ERROR] {str(e)}")

def update_film(id : int , new_data : dict):
    try:

        sem_correspondencia = True
        with open(DB_FILMS_ID, "r") as file:
            data = json.load(file)

        for film_id, item in data.items():

            if(film_id.isdigit()):
                if(int(film_id) == int(id)):
            
                    item['name'] = new_data['name']
                    item['description'] = new_data['description']
                    item['release_year'] = new_data['release_year']
                    item['length'] = new_data['length']
                    sem_correspondencia = False
                    break
        
        # 3. Write json file
        if(not sem_correspondencia):
            with open(DB_FILMS_ID, "w") as file:
                json.dump(data, file , indent=2)
            return "OK"
        else:
            return "O input não possui correspondência no banco de dados."

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def delete_film(id:int):

    try:
        with open(DB_FILMS_ID, "r") as file:
            data = json.load(file)

        keys = tuple(data.keys())
        for film_id in keys:
            if(film_id.isdigit()):
                if(int(film_id) == int(id)):
                    data.pop(film_id)
                
        # 3. Write json file
        with open(DB_FILMS_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def get_film(id):

    try:
        with open(DB_FILMS_ID, "r") as file:
            data = json.load(file)

        result = "Nenhum filme encontrado."
        for film_id , item in data.items():
            if(film_id.isdigit()):
                if(int(film_id) == int(id)):
                    result = item

    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return result

def get_all_films():

    try:
        data = "OK"
        with open(DB_FILMS_ID, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return data