# Food Database
 Database and shopping tool to track nutrition and spending

## How to update
1. Using the terminal, update recipes dataframe:
- cd documents
- cd food-database
- python3 add_recipe.py
Input recipe information by following the prompts.

2. Still in the terminal, update ingredients dataframe:
- python3 add_ingredient.py
Input ingredient information by following the prompts.

3. Staying in the terminal and in the food-database directory, update the recipes_ingredients dataframe:
- python3 add_recipe_ingredients.py
Input each ingredient for the recipe by following the prompts.

4. Get a new recipe file that contains all the nutrition info for each recipe, including your new one. Again staying inside the same directory:
- python3 update_recipes.py
As long as there are no errors, a new CSV file marked with todays date will appear in the recipes folder containing an updated record.


Once finished:
- git add .
- git commit -m ‘TODAYSDATE’
- git push

To-Do:
------
[x] Create script that prompts user when inputing new ingredient

[x] Create script that prompts user to input new recipe

[x] Create script that prompts user to input new recipe-ingredient combination
