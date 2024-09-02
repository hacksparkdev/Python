# Outline
import json
from pprint import pprint
recipes = []
# Add, edit, and delete recipe
new_recipe = [
    {
        "name" : 'Steak',

        "ingrdients":[
            '2 Steak',
            '1 bag of steak',
            '1 gallon of steak',
            '33 steaks'

        ],
        "Nutrition":{
            'Calories' : 68,
            'fat' : 5,
            'carbs' : 6,
            'protien': 6500
        },
        "Description":[
            "STEAK!"
        ]
    }
]

with open('recipes.json') as file:
    data = json.load(file)
    pprint(data)

    




#with open('recipes.json', 'w') as file:
#    json.dump(data, file, indent=4)




#nutrition_info = recipes[0]['Nutrition']
#for key, value in nutrition_info.items():
#    print(f"{key}: {value}")







#with open('recipes.json', 'w') as f:
#    json.dump(recipes, f, indent=4)



#for recipe in recipes[0]['ingrdients']:
#    print(recipe)


# Search for recipes by ingediaents or category


# Save and load recipe data from a file


