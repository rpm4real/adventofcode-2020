#%%
with open('d2/input.txt') as file: 
    pass_policies = file.read().split('\n')

pass_poli_lookup = [k.split(': ') for k in pass_policies]

#%%

success = 0 
for poli, password in pass_poli_lookup: 
    occur, letter = poli.split(' ')
    actual_occur = password.count(letter)
    min_occur, max_occur = occur.split('-')
    if occur >= min_occur and occur <= max_occur: 
        success += 1
    print(occur, letter)
    print(min_occur, max_occur)
    print(actual_occur)
    if success > 100: 
        break 
print(success)

# %%
