#%%
with open('d2/input.txt') as file: 
    pass_policies = file.read().split('\n')

pass_poli_lookup = [k.split(': ') for k in pass_policies]

#%%
# count cases where passwords contain character x times
success = 0 
for poli, password in pass_poli_lookup: 
    occur, letter = poli.split(' ')
    actual_occur = password.count(letter)
    min_occur, max_occur = occur.split('-')
    if actual_occur >= int(min_occur) and actual_occur <= int(max_occur): 
        success += 1

print(success)

# %%
# look for exactly one of the characters in string locations
success = 0 
for poli, password in pass_poli_lookup: 
    occur, letter = poli.split(' ')
    occurs = occur.split('-')
    checks = [password[int(spot)-1] == letter for spot in occurs]
    if any(checks) and not all(checks): 
        success += 1
print(success)
# %%
