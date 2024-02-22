import pandas as pd
import warnings
import datetime
import os
warnings.filterwarnings("ignore")

recipes = pd.read_csv('food_database/recipes-Recipes.csv')

# Prompt the user to add information for each column
new_row = {}
for column in recipes.columns:
    if column == 'recipe_id':
        new_row[column] = recipes['recipe_id'].max() + 1
    else:
        new_row[column] = input(f"Enter value for {column}: ")

        # # Prompt the user to change a column if they made a mistake
        # column_to_change = input("Did you make a mistake in any column? If yes, please enter the name of the column. If no, enter 'none': ")

        # if column_to_change != 'none':
        #     new_value = input(f"Enter the new value for {column_to_change}: ")
        #     new_row[column_to_change] = new_value


# Add the new row to the DataFrame
recipes = recipes.append(new_row, ignore_index=True)

# Output the DataFrame as a CSV file
recipes.to_csv('food_database/recipes-Recipes.csv', index=False)
