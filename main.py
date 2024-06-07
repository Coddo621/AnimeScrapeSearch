import anime_api
import os
from jikanpy import Jikan
import json

Jikan = Jikan()

anime_input = input('Enter anime name: ')

search_result = Jikan.search('anime', anime_input)

key_list = list(search_result.keys())

#print(key_list)


for i in range(len(search_result["data"])):
    print(i+1, ". ", search_result["data"][i]["title"])

choice_input = int(input("Input the number of the series you would like to view: "))

data = search_result["data"][choice_input - 1]

anime = data["mal_id"]
episodes = data["episodes"]
anime_name = data["title"]
series_type = data["type"]
series_status = data["status"]

print("\nName: ", anime_name)
print("Series Type: ", series_type)
print("ID: ", anime)
print("Episodes: ", episodes)
print("Status: ", series_status)
