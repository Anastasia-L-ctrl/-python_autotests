import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'токен тренера'
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN} 
#body_create = {
    #"name": "имя покемона",
    #"photo_id": номер картинки
#}

#response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
#print(response_create.text)

#message = response_create.json()['message']
#print(message)

#body_update = {

    #"pokemon_id": "айди покемона",
    #"name": "новое имя покемона",
    #"photo_id": номер картинки
#}

#response_update=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_update)
#print(response_update.json())

body_catch = {
    "pokemon_id": "айди покемона"
}
response_catch=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.json())
