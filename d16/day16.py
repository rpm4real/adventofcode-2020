#%% 
with open('input.txt') as file: 
    cheat_sheet = file.read().split('\n') 

rules = [line for line in cheat_sheet if 'or' in line]
tickets_list = cheat_sheet[cheat_sheet.index('nearby tickets:')+1:]

# %%
rule_dict = {}
for rule in rules: 
    key, val = rule.split(': ')
    rule_dict[key] = [list(map(int,rang.split('-'))) for rang in val.split(' or ')]
# %%
tickets_array = [list(map(int,ticket.split(','))) for ticket in tickets_list]
# %%
def check_field(field): 
    for rule_ranges in rule_dict.values(): 
        for rang in rule_ranges: 
            if field >= rang[0] and field <= rang[1]: 
                return 0 
    return field
                

def check_ticket(ticket): 
    ticket_error = []
    for field in ticket: 
        ticket_error.append(check_field(field))
    return sum(ticket_error)

ticket_error_sum = 0
for ticket in tickets_array: 
    ticket_error_sum += check_ticket(ticket)

ticket_error_sum
#%%
# part 2 
import pandas as pd 
import numpy as np
# %%
rule_df = pd.DataFrame(rule_dict).melt(var_name='field_name') #.pivot(index = 'variable', columns = 'value') 
rule_df['value_min'] = rule_df['value'].apply(lambda x: x[0])
rule_df['value_max'] = rule_df['value'].apply(lambda x: x[1])
rule_df['range_num'] = rule_df.groupby('field_name')['value_min'].rank()
rule_df = rule_df.drop('value', axis = 1)
rule_df = rule_df.pivot_table(index = 'field_name', columns = 'range_num').reset_index()
#rule_df.columns = ['_'.join(str(col)).strip() for col in rule_df.columns.values]
rule_df.columns = ['field_name','max_1','max_2', 'min_1','min_2']
# %%
ticket_df = pd.DataFrame(tickets_array).reset_index().rename(columns={'index':'ticket'})

# %%
ticket_melt = ticket_df.melt(id_vars='ticket', var_name='field', value_name='field_val')
#ticket_melt[ticket_melt['ticket']==1]
# %%
ticket_melt['key'] = 1
rule_df['key'] = 1
merge_df = ticket_melt.merge(rule_df, on='key')
#merge_df = merge_df[(merge_df['field_val']>=merge_df['value_min']) & ((merge_df['field_val']<=merge_df['value_max']))].copy()
low_cond_1 = merge_df['field_val']>=merge_df['min_1']
low_cond_2 = merge_df['field_val']>=merge_df['min_2']
high_cond_1 = merge_df['field_val']<=merge_df['max_1']
high_cond_2 = merge_df['field_val']<=merge_df['max_2']
merge_df = merge_df[(low_cond_1 & high_cond_1) | (low_cond_2 & high_cond_2)].copy()
merge_df = merge_df.drop('key', axis = 1)

# %%
cnt_fields = merge_df.groupby('ticket').agg({
    'field': lambda x: x.nunique()
}) #.reset_index().groupby('field')['ticket'].count()
correct_tickets = cnt_fields[cnt_fields['field']==20].index

# %%
merge_df_mapping = merge_df[merge_df['ticket'].isin(correct_tickets)].groupby(['field_name','field']).agg({
    'field_val': np.size
}).reset_index()
# %%
