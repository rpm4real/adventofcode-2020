#%%
with open('input.txt') as file: 
    seat_layout = [list(l) for l in file.read().split('\n')]

def check_adjacents(layout,i,j): 
    adj_vals = []
    for flip1 in [-1,0,1]: 
        for flip2 in [-1,0,1]: 
            if i+flip1 >= 0 and j+flip2 >= 0 and i+flip1 < len(layout) and j+flip2 < len(layout[i]): 
                adj_vals.append(layout[i+flip1][j+flip2])
    adj_vals.remove(layout[i][j])
    return {char:adj_vals.count(char) for char in ['.','L','#']}

def fix_print(row): 
    strs = ''
    for k in row: 
        strs += k 
    print(strs)

#%% 
from copy import deepcopy
prev_layout = []
new_layout = deepcopy(seat_layout)
cnt = 0
while new_layout != prev_layout :
    cnt += 1
    prev_layout = deepcopy(new_layout)
    for i,row in enumerate(prev_layout): 
        for j,element in enumerate(row): 
            adj = check_adjacents(prev_layout,i,j)
            if element == 'L' and adj['#'] == 0: 
                new_layout[i][j] = '#'
            elif element == '#' and adj['#'] > 3: 
                new_layout[i][j] = 'L'

#%% 
cntl = 0 
for row in prev_layout: 
    for j in row: 
        if j == '#': cntl += 1 
print(cntl)

