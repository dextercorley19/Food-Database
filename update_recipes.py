import pandas as pd
import warnings
import datetime
import os
warnings.filterwarnings("ignore")

ingredients = pd.read_csv('food_database/ingredients-Ingredients.csv')
ingredients_recipes = pd.read_csv('food_database/recipe-ingredient-recipe_ingredient.csv')
recipes = pd.read_csv('food_database/recipes-Recipes.csv')

ingredients.rename(columns={'Ingredient_id': 'ingredient_id'}, inplace=True)
recipe_ingredient_ingredients = ingredients_recipes.merge(ingredients, on='ingredient_id', how='left')
recipe_ingredient_ingredients['scalar'] = recipe_ingredient_ingredients.apply(lambda row: row['Quantity'] / row['serving_size'], axis=1)
recipe_ingredient_ingredients['calories_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['calories_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['carbohydrates_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['carbohydrates_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['dietary_fiber_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['dietary_fiber'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['sugar_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['sugar_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['added_sugar_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['added_sugar_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['protein_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['protein_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['polyunsaturated_fat_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['polyunsaturated_fat_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['monounsaturated_fat_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['monounsaturated_fat_per_unit'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['saturated_fat_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['saturated_fat'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['total_fat_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['total_fat'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['Cholesterol_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['Cholesterol'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['sodium_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['sodium_per_serving'] * row['scalar'], axis=1)
recipe_ingredient_ingredients['price_per_dish'] = recipe_ingredient_ingredients.apply(lambda row: row['price_per_serving'] * row['scalar'], axis=1)
recipe_stats = recipe_ingredient_ingredients.groupby('recipe_id').sum().reset_index()
recipe_stats_to_move = pd.DataFrame(recipe_stats, columns=['recipe_id',
    'calories_per_dish',
    'carbohydrates_per_dish', 'dietary_fiber_per_dish', 'sugar_per_dish',
    'added_sugar_per_dish', 'protein_per_dish',
    'polyunsaturated_fat_per_dish', 'monounsaturated_fat_per_dish',
    'saturated_fat_per_dish', 'total_fat_per_dish', 'Cholesterol_per_dish',
    'sodium_per_dish', 'price_per_dish'])
recipes = recipes.merge(recipe_stats_to_move, how='left', on='recipe_id')
recipes = recipes.drop_duplicates()
recipes['calories_per_serving'] = recipes.apply(lambda row: row['calories_per_dish'] / row['Servings'], axis=1)
recipes['carbohydrates_per_serving'] = recipes.apply(lambda row: row['carbohydrates_per_dish'] / row['Servings'], axis=1)
recipes['dietary_fiber_per_serving'] = recipes.apply(lambda row: row['dietary_fiber_per_dish'] / row['Servings'], axis=1)
recipes['sugar_per_serving'] = recipes.apply(lambda row: row['sugar_per_dish'] / row['Servings'], axis=1)
recipes['added_sugar_per_serving'] = recipes.apply(lambda row: row['added_sugar_per_dish'] / row['Servings'], axis=1)
recipes['protein_per_serving'] = recipes.apply(lambda row: row['protein_per_dish'] / row['Servings'], axis=1)
recipes['polyunsaturated_fat_per_serving'] = recipes.apply(lambda row: row['polyunsaturated_fat_per_dish'] / row['Servings'], axis=1)
recipes['monounsaturated_fat_per_serving'] = recipes.apply(lambda row: row['monounsaturated_fat_per_dish'] / row['Servings'], axis=1)
recipes['saturated_fat_per_serving'] = recipes.apply(lambda row: row['saturated_fat_per_dish'] / row['Servings'], axis=1)
recipes['total_fat_per_serving'] = recipes.apply(lambda row: row['total_fat_per_dish'] / row['Servings'], axis=1)
recipes['Cholesterol_per_serving'] = recipes.apply(lambda row: row['Cholesterol_per_dish'] / row['Servings'], axis=1)
recipes['sodium_per_serving'] = recipes.apply(lambda row: row['sodium_per_dish'] / row['Servings'], axis=1)
recipes['price_per_serving'] = recipes.apply(lambda row: row['price_per_dish'] / row['Servings'], axis=1)

recipes = recipes.drop(['Unnamed: 8'], axis=1)

# Get today's date
today = datetime.date.today()

# Create the folder if it doesn't exist
folder_name = 'recipes'

# Output the recipes dataframe as a CSV file with today's date as a suffix
file_name = f'recipes_{today}.csv'
file_path = os.path.join(folder_name, file_name)
recipes.to_csv(file_path, index=False)
