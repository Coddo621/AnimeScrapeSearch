import anime_api
import os
from jikanpy import Jikan
import json
from anime_api.apis import AnimechanAPI

class scrape_app():
    def __init__(self):
        self.jikan = Jikan()
        self.anime_quote = AnimechanAPI()

    def format_dict(self, data, indent=4, level=0):
        indent_space = ' ' * indent * level
        for key, value in data.items():
            formatted_key = key.replace('_', ' ').capitalize()
            if not value:
                pass
            elif isinstance(value, (str, int, float)):
                print(f"{indent_space}{formatted_key}: {value}")
            elif isinstance(value, list):
                print(f"{indent_space}{formatted_key}:")
                self.format_list(value, indent, level + 1)
            elif isinstance(value, dict):
                print(f"{indent_space}{formatted_key}:")
                self.format_dict(value, indent, level + 1)

    def format_list(self, data, indent=4, level=0):
        indent_space = ' ' * indent * level
        for item in data:
            if isinstance(item, dict):
                self.format_dict(item, indent, level)
            else:
                print(f"{indent_space}- {item}")


    def scrape_anime_info(self, anime_input):
        search_result = self.jikan.search('anime', anime_input)
        for i in range(len(search_result["data"])):
            print(f"{i + 1}. {search_result['data'][i]['title']}")
        
        choice_input = int(input("\nInput the number of the series you would like to view: "))
        data = search_result["data"][choice_input - 1]
        self.format_dict(data)
        print("\n")

    def random_anime_quote(self):
        quote_reference = self.anime_quote.get_random_quote()
        print(f"Anime: {quote_reference.anime}\nCharacter: {quote_reference.character}\nQuote: {quote_reference.quote}")

print("1. Anime search scrape\n2. Random anime quote")

module_choice = int(input("Choose which scrape module you want to use: "))
match module_choice:
    case 1:
        anime_input = input("Enter anime name: ")
        scrape_app_instance = scrape_app()
        scrape_app_instance.scrape_anime_info(anime_input)
    case 2:
        scrape_app_instance = scrape_app()
        scrape_app_instance.random_anime_quote()
    case _:
        print("Please input a valid option")