# Food Database
 Database and shopping tool to help track my nutrition and spending

## How to update

In food_database folder (using numbers):
1. Add new ingredients to ingredient table
2. Add new recipe ingredient combinations in recipe-ingredient table
3. Add new recipe in recipe table

Once updated, in command line:
- cd documents
- cd food-database
- python3 update_recipes.py
- git add .
- git commit -m ‘TODAYSDATE’
- git push

A new version of the recipes table with nutrition facts and prices will appear in the recipes folder with todays date.
