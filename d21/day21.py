#%% 
import pandas as pd
with open('input.txt') as file: 
    recipe_lines = file.read().split('\n')

recipe_df = pd.DataFrame([line.split(' (contains ') for line in recipe_lines], columns = ['ingredients', 'allergens'])
# %%
recipe_df['allergens'] = recipe_df['allergens'].str.strip(' )')
#recipe_df = recipe_df.reset_index().rename(columns={'index':'recipe_id'})
# %%
recipe_df = recipe_df.assign(ingredients=recipe_df.ingredients.str.split(" ")).explode('ingredients')
recipe_df = recipe_df.assign(allergens=recipe_df.allergens.str.split(",")).explode('allergens')
#%% 
recipe_df = recipe_df.reset_index().rename(columns={'index':'recipe_id'})
# %%
import numpy as np
# potential allergen and ingredient matchup 
ing_aller_match = recipe_df.groupby(['ingredients', 'allergens']).agg({
    'recipe_id': np.size
}).reset_index()

# total number of times an ingredient is used in a recipe
ing_rec_cnt = recipe_df.groupby('ingredients').agg({
    'recipe_id': np.size 
}).reset_index

# if an ingredient is an allergen, recipe-allergen occurances will equal recipe occurances

# %%
