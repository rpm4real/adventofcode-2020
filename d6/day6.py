#%%
import pandas as pd
with open('input.txt') as file: 
    groups = file.read().split('\n\n')
    group_list = [(k,g.split('\n')) for k,g in enumerate(groups)]

group_df = pd.DataFrame(group_list, columns=['group','answers']).explode('answers')
# %%

group_gp = group_df.groupby('group')[['answers']].sum()
group_gp['nunique'] = group_gp['answers'].apply(set).apply(len)

group_gp['nunique'].sum()


# %%
