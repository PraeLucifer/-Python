import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'c76b84b89ffaf7f00768d93c50537b08'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "33803"


def test_status_code():
    response = requests.get(url = f'{URL}pokemons', params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Фуксия'

def test_trainers_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainers_name():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == "Moonlight"


