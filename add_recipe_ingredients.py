import pandas as pd
import warnings
import datetime
import os
warnings.filterwarnings("ignore")

recipes_ingredients = pd.read_csv('food_database/recipe-ingredient-recipe_ingredient.csv')
ingredients = pd.read_csv('food_database/ingredients-Ingredients.csv')
recipes = pd.read_csv('food_database/recipes-Recipes.csv')

# Prompt the user to enter ingredient names and amounts
ingredients['category'] = ingredients['category'].str.lower()
recipes['category'] = recipes['category'].str.lower()

while True:
    recipe_name = input("Enter recipe name (or 'done' to finish): ")
    if recipe_name == 'done':
        break

    # Check if the entered recipe name exists in the recipes DataFrame
    matched_recipes = recipes[recipes['category'] == recipe_name]
    if len(matched_recipes) == 0:
        print(f"Recipe '{recipe_name}' not found.")
        continue

    # If the recipe exists, get its recipe_id
    recipe_id = matched_recipes.iloc[0]['recipe_id']

    while True:
        ingredient_name = input("Enter ingredient name: ")

        # Check if the entered ingredient name exists in the ingredients DataFrame
        matched_ingredients = ingredients[ingredients['category'] == ingredient_name]
        if len(matched_ingredients) == 0:
            print(f"Ingredient '{ingredient_name}' not found.")
            continue  # Continue to the next iteration of the loop to allow the user to try again

        # If the ingredient exists, get its ingredient_id
        ingredient_id = matched_ingredients.iloc[0]['Ingredient_id']
        measurement_units = input("Enter measurement units for ingredient serving size: ")
        ingredient_quantity = input("Enter ingredient amount: ")
        ingredient_notes = input("Enter notes about ingredient in this recipe (ex: chopped) ('ENTER' to skip): ")
        ingredient_optional = input("Is this optional? (1/0): ")
        ingredient_step = input("What step is this ingredient used?: ")

        # Add the ingredient entry to the recipes_ingredients list
        ingredient_entry = {
            'recipe_id': recipe_id,
            'ingredient_id': ingredient_id,
            'Quantity': ingredient_quantity,
            'measurement_unit': measurement_units,
            'Notes': ingredient_notes,
            'is_optional': ingredient_optional,
            'step_number': ingredient_step
        }
        recipes_ingredients = recipes_ingredients.append(ingredient_entry, ignore_index=True)
        recipes_ingredients.to_csv('food_database/recipe-ingredient-recipe_ingredient.csv', index=False)
        break


