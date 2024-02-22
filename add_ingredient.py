import pandas as pd
import warnings
import datetime
import os
warnings.filterwarnings("ignore")

ingredients = pd.read_csv('food_database/ingredients-Ingredients.csv')

# Prompt the user to add information for each column
new_row = {}
for column in ingredients.columns:
    if column == 'Ingredient_id':
        new_row[column] = ingredients['Ingredient_id'].max() + 1
    else:
        new_row[column] = input(f"Enter value for {column}: ")


        # # Prompt the user to change a column if they made a mistake
        # column_to_change = input("Did you make a mistake in any column? If yes, please enter the name of the column. If no, enter 'none': ")

        # if column_to_change != 'none':
        #     new_value = input(f"Enter the new value for {column_to_change}: ")
        #     new_row[column_to_change] = new_value


# Add the new row to the DataFrame
ingredients = ingredients.append(new_row, ignore_index=True)

# Output the DataFrame as a CSV file
ingredients.to_csv('food_database/ingredients-Ingredients.csv', index=False)
