#%%
with open('input_debug.txt') as file: 
    initial_states = file.read().split('\n') 

cube_array = {}
for row,line in enumerate(initial_states): 
    for col,state in enumerate(line): 
        #cube_array.append(CubeState(col, row, 0, state))
        cube_array[(col, row, 0)] = state 


# %%
from itertools import product

def coord_add(coord1, coord2): 
    return tuple((x + y for x,y in zip(coord1, coord2)))

def check_adjacents(coordinate, my_array): 
    """return number of active adjacent coordinates"""
    neighborhood = [-1,0,1]
    search_look = product(neighborhood, repeat = 3)
    adj_values = 0
    search_space = [coord_add(coordinate,d) for d in search_look if d != (0,0,0)]
    f = lambda x: 1 if x == '#' else 0 
    return sum([f(my_array.get(coord,'.')) for coord in search_space])

def fill_array(my_array): 

    from functools import reduce 
    mins = reduce(lambda x,y: [min(x[k], y[k]) for k in range(3)], cube_array)
    maxs = reduce(lambda x,y: [max(x[k], y[k]) for k in range(3)], cube_array)
    for k, layers in enumerate(zip(mins, maxs)): 
        coord_add( , (1,0,0) )
    
    for p in product([0,1],repeat = 3): 
        my_array[coord_add(mins,(-x for x in p))] = '.'
        my_array[coord_add(maxs, p)] = '.'
    return my_array

def sim_cycle(my_array):
    #new_array = fill_array(my_array)
    check_coords = [k for k in my_array.items()]
    #for loc,state in check_coords: 
    while COND: 
        num_active = check_adjacents(loc, my_array)
        if state == '#':  
            if num_active in (2,3):
                new_state = '#'
            else: 
                new_state = '.'
        
        elif state == '.' and num_active == 3:  
            new_state = '#'
        else: 
            new_state = '.'
        new_array[loc] = new_state
        #new_array = {**new_array, **fill_cube_array}
    return new_array

#%% 
for k in range(2): 
    cube_array = sim_cycle(cube_array)
    print(list(cube_array.values()).count('#'))

# %%
list(cube_array.values()).count('#')


# %%
##########
neighborhood = [-1,0,1]
check_coords = [k for k in cube_array.items()]
# %%
def print_cube(my_array): 
    zrange = [coord[2] for coord in my_array.keys()]
    min_z, max_z = min(zrange), max(zrange)
    for z in range(min_z, max_z+1): 
        print('z={0}'.format(z))
        print_range = [coord for coord in my_array.keys() if coord[2] == z]