#%%
with open('input.txt') as file: 
    initial_states = file.read().split('\n') 

cube_array = {}
for row,line in enumerate(initial_states): 
    for col,state in enumerate(line): 
        #cube_array.append(CubeState(col, row, 0, state))
        cube_array[(col, row, 0)] = state 

# %%
from collections import Counter 
from itertools import product

neighborhood = [c for c in list(product([-1,0,1], repeat = 3)) if c != (0,0,0)]

#could define this better 
initial_state = set([k for k in cube_array.keys() if cube_array[k]=='#'])

def shift(cells, delta):
    "shift cells by a delta"
    (dx, dy, dz) = delta
    return {(x+dx, y+dy, z+dz) for (x, y, z) in cells}

def sim_cycle(state, N):
    "iterate cycle N times"
    for g in range(N):
        counts = Counter(n for c in state for n in shift(neighborhood, c))
        state = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in state)}
    return state 


# %%
active_states = sim_cycle(initial_state, 6)
len(active_states)
# %%
# part 2 
neighborhood = [c for c in list(product([-1,0,1], repeat = 4)) if c != (0,0,0,0)]

#could define this better 
initial_state = set([k + (0,) for k in cube_array.keys() if cube_array[k]=='#'])

def shift2(cells, delta):
    "shift cells by a delta"
    (dx, dy, dz, dw) = delta
    return {(x+dx, y+dy, z+dz, w+dw) for (x, y, z, w) in cells}

def sim_cycle2(state, N):
    "iterate cycle N times"
    for g in range(N):
        counts = Counter(n for c in state for n in shift2(neighborhood, c))
        state = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in state)}
    return state 


# %%
active_states = sim_cycle2(initial_state, 6)
len(active_states)
# %%
