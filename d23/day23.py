#%% 
from collections import deque

cup_string = '284573961'
#cup_string = '389125467'#DEBUG
cup_array = deque([int(c) for c in cup_string])

# %%
def cup_move(my_cup_array): 
    my_cup_array.rotate(-1)
    shifted = []
    for k in range(3): 
        shifted.append(my_cup_array.popleft())
    #print('pickup: ', shifted)
    my_cup_array.rotate(1)
    next_index = find_destination(my_cup_array)
    #print('array with removed cups: ', cup_array)
    #print('destination: ', next_index)
    for k,s in enumerate(shifted): 
        my_cup_array.insert(next_index + (k+1), s) 
    my_cup_array.rotate(-1)
    return my_cup_array


def find_destination(my_cup_array): 
    check_val = my_cup_array[0] - 1 
    while True:
        if check_val in my_cup_array: 
            return my_cup_array.index(check_val)
        elif check_val < min(my_cup_array):
            check_val = max(my_cup_array)
        else: 
            check_val -= 1
# %%
for turn in range(100): 
    cup_array = cup_move(cup_array)

cup_array.rotate(cup_array.index(1)*-1)

# %%
from functools import reduce
reduce(lambda x,y: x+y, [str(k) for k in cup_array])
# %%
