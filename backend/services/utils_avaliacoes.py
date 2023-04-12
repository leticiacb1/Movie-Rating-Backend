import os
import json
from dotenv import load_dotenv

load_dotenv()
DB_AVALIACAO_ID = os.getenv('DB_RATING_PATH')
DB_FILMS_ID = os.getenv('DB_FILMS_PATH')

def create_rating(new_data):
    try:
        # 1. Read
        with open(DB_AVALIACAO_ID) as file:
            data = json.load(file)

        dict_data = new_data.dict()

        # Verifica se film_id existe na base de filmes
        sem_correspondencia = True
        with open(DB_FILMS_ID) as file:
            data_film = json.load(file)
        
        for film_id in data_film.keys():
            if(film_id.isdigit()):
                if(int(film_id) == int(dict_data['film_id'])):
                    sem_correspondencia = False
                    break
        
        # 2. Update json object
        if(not sem_correspondencia):    
            id = int(data['count_id']) + 1
            data.update({str(id) : dict_data})

            # Atualiza controle de count_id:
            data['count_id'] = id

            # 3. Write
            with open(DB_AVALIACAO_ID, "w") as file:
                json.dump(data, file , indent=2)

            return "OK"
        else:
            return f"id_film = '{dict_data['film_id']}' não possui correspondencia na base de filmes"

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def update_rating(id : int , new_data : dict):
    try:

        sem_correspondencia = True
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        for rating_id, item in data.items():

            if(rating_id.isdigit()):
                if(int(rating_id) == int(id)):
                    
                    item['film_id'] = new_data['film_id']
                    item['comment'] = new_data['comment']
                    item['score'] = new_data['score']
                    sem_correspondencia = False
                    break
        
        # 3. Write json file
        if(not sem_correspondencia):
            with open(DB_AVALIACAO_ID, "w") as file:
                json.dump(data, file , indent=2)
            return "OK"
        else:
            return "O input não possui correspondência no banco de dados."

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def delete_rating(id:int):

    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        keys = tuple(data.keys())
        for rating_id in keys:
            if(rating_id.isdigit()):
                if(int(rating_id) == int(id)):
                    data.pop(rating_id)
                
        # 3. Write json file
        with open(DB_AVALIACAO_ID, "w") as file:
            json.dump(data, file , indent=2)

    except Exception as e:
        print(f" [ERROR] {str(e)}")

def get_rating(id):

    try:
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)

        result = "Nenhum filme encontrado."
        for rating_id , item in data.items():
            if(rating_id.isdigit()):
                if(int(rating_id) == int(id)):
                    result = item

    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return result

def get_all_rating():

    try:
        data = "OK"
        with open(DB_AVALIACAO_ID, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f" [ERROR] {str(e)}")
        
    return data