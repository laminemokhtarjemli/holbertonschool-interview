import requests
import sys

movie_id = sys.argv[1]
response = requests.get(f"https://swapi.dev/api/films/{movie_id}")

characters = response.json()['characters']

for character in characters:
  character_response = requests.get(character)
  character_name = character_response.json()['name']
  print(character_name)
