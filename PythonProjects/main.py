import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'c76b84b89ffaf7f00768d93c50537b08'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']


body_change_name = {
    "pokemon_id": pokemon_id ,
    "name": "Фуксия",
    "photo_id": 3
}

response_change_name = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
