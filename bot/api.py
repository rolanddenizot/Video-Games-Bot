import requests
from igdb.wrapper import IGDBWrapper
import os
import json
import datetime

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']


response = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials')
json_resp = response.json()
access_token = json_resp["access_token"]

wrapper = IGDBWrapper(client_id, access_token)

def getGameName(game_name):
  byte_array = wrapper.api_request('games',f'fields name; search "{game_name}";')
  data = bytesToJson(byte_array)
  api_name = data[0]['name']
  return api_name
  
def getGameInfo(game_name):
  game_info = ''
  byte_array = wrapper.api_request('games',f'fields summary,storyline; search "{game_name}";')
  data = bytesToJson(byte_array)
  del data[0]['id']
  summary = data[0]['summary']
  if 'storyline' in data[0].keys():
    storyline = data[0]['storyline']
    game_info = f'**Game summary:** \n{summary}\n**Game storyline:** \n{storyline}'
  else:
    game_info = f'**Game summary:** \n{summary}'
  return game_info

def getReleaseDate(game_name):
  release_date = None
  byte_array = wrapper.api_request('games',f'fields first_release_date; search "{game_name}";')
  data = bytesToJson(byte_array)
  del data[0]['id']
  s = data[0]['first_release_date']
  dt = datetime.datetime.fromtimestamp(s)
  release_date = dt.strftime("%Y/%m/%d")
  return release_date

def getGenres(game_name):
  byte_array = wrapper.api_request('games',f'fields genres; search "{game_name}";')
  data_game = bytesToJson(byte_array)
  # print(data_game)
  id_genre = data_game[0]['genres'][0]
  # print(id_genre)
  byte_array = wrapper.api_request('genres',f'fields name; where id = {id_genre};')
  data_genre = bytesToJson(byte_array)
  # print(data_genre)
  genre_name = data_genre[0]['name']
  return genre_name
  
def getInvolvedCompanies(game_name):
  byte_array = wrapper.api_request('games',f'fields involved_companies; search "{game_name}";')
  data_game = bytesToJson(byte_array)
  involved_companies_ids = data_game[0]['involved_companies']

  bytes_involved_companies = [wrapper.api_request('involved_companies',f'fields company ; where id = {id};')for id in involved_companies_ids]
  data_companies = [bytesToJson(b) for b in bytes_involved_companies]
  companies_ids = [d[0]['company'] for d in data_companies]

  bytes_companies = [wrapper.api_request('companies',f'fields name; where id = {id};') for id in companies_ids]
  data_companies = [bytesToJson(b) for b in bytes_companies]
  name_companies = [d[0]['name'] for d in data_companies]
  
  str_companies = f'The involved companies for **{game_name}** are: \n'+''.join(f'{n}, 'for n in name_companies)
  str_companies = str_companies[:-2]
  return str_companies

def bytesToJson(byte_array):
  json_str = byte_array.decode('utf8').replace("'", '"')
  json_data = json.loads(json_str)
  return json_data

# game_info = getGameInfo("Halo")
# print(game_info)
# companies = getInvolvedCompanies("Halo")
# print(companies)
#game_genre = getGenres("Halo")
#print(game_genre)
