#%%
with open('input.txt') as file: 
    slope = file.read().split('\n')

def follow_slope(down, over): 
    tree, col = 0, 0 
    width = len(slope[0])
    for row in slope[::down]: 
        if row[col % width] == '#': tree += 1
        col += over 
    return tree


#%% 
# part 1 
print(follow_slope(1,3))

# %%
# part 2 
from functools import reduce
steps = [(1,1), (1,3), (1,5), (1,7), (2,1)]
tree_list = [follow_slope(down,over) for down,over in steps]
print(reduce(lambda x,y: x*y, tree_list))

