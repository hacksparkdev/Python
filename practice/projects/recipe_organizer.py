# Outline
import json

# Add, edit, and delete recipe
recipes = [
    {
        "name" : 'Hotdogs',

        "ingrdients":[
            '1 pack of hotdogs',
            '1 pot',
            '1 can of chille'

        ],
        "Nutrition":{
            'Calories' : 50,
            'fat' : 9,
            'carbs' : 63,
            'protien': 65
        },
        "Description":[
            "American style hotdogs, Want to take years off of your life Eat these beautifuly awful hotdogs "
        ]
    }
]

with open('recipes.json', 'w') as file:
    json.dump(recipes, file, indent=4)

#nutrition_info = recipes[0]['Nutrition']
#for key, value in nutrition_info.items():
#    print(f"{key}: {value}")







#with open('recipes.json', 'w') as f:
#    json.dump(recipes, f, indent=4)



#for recipe in recipes[0]['ingrdients']:
#    print(recipe)


# Search for recipes by ingediaents or category


# Save and load recipe data from a file


