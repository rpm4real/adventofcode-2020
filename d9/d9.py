#%%
with open('input.txt') as file: 
    code = [int(x) for x in file.read().split('\n')]

#%% 
# part 1 
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
# part 2 
target = val 
found = False 
start = 0 
end = 1 
while found is False: 
    check_range = code[start:end]
    if sum(check_range) < target: 
        end += 1 
    elif sum(check_range) > target: 
        start += 1
    else: 
        found = True 

print(min(check_range), max(check_range))
# %%
print(min(check_range)+max(check_range))
# %%
