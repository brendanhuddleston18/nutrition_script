import requests
import json

ingredients = ["blueberries", "strawberries", "almond milk"]


def get_nutrition_data(ingredient):
    response = requests.get(f'https://api.edamam.com/api/nutrition-data?app_id=22eb6145&app_key=%20b4e0e731b77176135ba3b820c7bf1ac8&nutrition-type=cooking&ingr={ingredient}')
    data = response.json()
    print(data)

get_nutrition_data(ingredients[1])