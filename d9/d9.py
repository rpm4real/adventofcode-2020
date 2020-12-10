#%%
with open('input.txt') as file: 
    code = [int(x) for x in file.read().split('\n')]

#%% 


look_back = 25 
for k, val in enumerate(code[look_back:], start = look_back):
    look_back_range = code[k - look_back:k]
    for check_sum in look_back_range[::-1]: 
        if val - check_sum in look_back_range: 
            passed = True
            break 
        else: 
            passed = False 
    if not passed: 
        break 

print(val, k)
# %%
