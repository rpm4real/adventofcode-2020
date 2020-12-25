#%%
import re 
with open('input.txt') as file: 
    pass_file = file.read().split('\n\n')

parse1 = [re.split('\s', p) for p in pass_file]

#%%
pass_list = []
for passport in parse1: 
    mydict = {}
    for field in passport: 
        fields = field.split(':')
        mydict[fields[0]] = fields[1]
    pass_list.append(mydict)

# %%

pass_cnt = 0 
for passport in pass_list: 
    if len(passport) == 8: 
        pass_cnt += 1 
    elif len(passport) == 7 and 'cid' not in passport:   
        pass_cnt +=1 

print(pass_cnt)

#%% 
import pandas as pd 

# %%
pass_df = pd.DataFrame(pass_list)

#%% 
def check_hgt(row):
    if 'cm' in row: 
        val = int(row.split('cm')[0])
        return (val >= 150) and (val <= 193)
    elif 'in' in row: 
        val = int(row.split('in')[0])
        return (val >= 59) and (val <= 76)
    else: 
        return False 

birth_rule = (pd.to_numeric(pass_df['byr']) >= 1920) & (pd.to_numeric(pass_df['byr'])  <= 2002)
issue_rule = (pd.to_numeric(pass_df['iyr'])  >= 2010) & (pd.to_numeric(pass_df['iyr'])  <= 2020)
exp_rule = (pd.to_numeric(pass_df['eyr'])  >= 2020) & (pd.to_numeric(pass_df['eyr'])  <= 2030)
hgt_rule = pass_df['hgt'].apply(str).apply(check_hgt)
hcl_rule = pass_df['hcl'].str.fullmatch(pat = '#([a-f]|[0-9])*')
eye_rule = pass_df['ecl'].isin(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
pid_rule = (pass_df['pid'].str.len() == 9) & (pass_df['pid'].str.isnumeric())


# %%
pass_df[birth_rule & issue_rule & exp_rule & hgt_rule & hcl_rule & eye_rule & pid_rule ]
# %%
