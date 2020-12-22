#%% 
import pandas as pd
with open('input.txt') as file: 
    recipe_lines = file.read().split('\n')

def renamer(agg_func,desired_name):
    def return_func(x):
        return agg_func(x)
    return_func.__name__ = desired_name
    return return_func
#%% 
recipe_df = pd.DataFrame([line.split(' (contains ') for line in recipe_lines], columns = ['ingredients', 'allergens'])
# %%
recipe_df['allergens'] = recipe_df['allergens'].str.strip(' )')
#recipe_df = recipe_df.reset_index().rename(columns={'index':'recipe_id'})
# %%
recipe_df = recipe_df.assign(ingredients=recipe_df.ingredients.str.split(" ")).explode('ingredients')
recipe_df = recipe_df.assign(allergens=recipe_df.allergens.str.split(", ")).explode('allergens')
#%% 
recipe_df = recipe_df.reset_index().rename(columns={'index':'recipe_id'})
# %%
import numpy as np

#%% 
u_ingredient = recipe_df.groupby('ingredients').count().reset_index()[['ingredients']].assign(key=1)
u_allergen = recipe_df.groupby('allergens').count().reset_index()[['allergens']].assign(key=1)
cj_all_ing = u_ingredient.merge(u_allergen, on = 'key').drop('key', axis=1)


# %%
candidates = {}
for allergen in u_allergen['allergens']: 
    temp_df = recipe_df[recipe_df['allergens']==allergen].copy()
    temp_gp = temp_df.groupby('ingredients')['recipe_id'].count()
    candidates[allergen] = set(temp_gp[temp_gp == max(temp_gp)].index)

ingd = set(u_ingredient['ingredients']).difference(set.union(*[s for s in candidates.values()]))
# %%
# number of rows 
recipe_df[recipe_df['ingredients'].isin(ingd)].groupby(['ingredients','recipe_id']).count().count()

# %%
#part 2 
final_lookup = {}
known = []
while len(known) < len(candidates):
    for key, val in candidates.items(): 
        if len(val) == 1: 
            l = next(iter(val))
            final_lookup[key] = l
            known.append(l)
        else: 
            differ_known = val.difference(set(known))
            if len(differ_known) == 1: 
                l = next(iter(differ_known))
                final_lookup[key] = l
                known.append(l)
            
        

# %%
alg_sorted = sorted(final_lookup.keys())
final_str = ''
for alg in alg_sorted: 
    final_str = final_str + final_lookup[alg] + ','

final_str 
# %%
