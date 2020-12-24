#%% 
with open('input.txt') as file: 
    tile_directions = file.read().split('\n')

# %%
origin = (0, 0, 0) #e/w, ne/sw, nw/se 
def coord_add(x, y): 
    return tuple((dx + dy for dx, dy in zip(x,y)))

#great code that I never used.
#dir_index = ['e','w','ne','sw','nw','se'].index(direction)
#dir_vec = [int(el==(dir_index//2))*(1 - 2*(dir_index % 2)) for el in range(3)]

def dir_add_hex(direction, coord): 
    dir_lookup = {
        'e': (1, -1, 0), 
        'w': (-1, 1, 0), 
        'ne': (1, 0, -1), 
        'sw': (-1, 0, 1), 
        'nw': (0, 1, -1), 
        'se': (0, -1, 1)
    }
    return coord_add(dir_lookup[direction],coord)
   
def direction_split(chars): 
    if len(chars) == 1: 
        return chars 
    elif chars in ['ne', 'nw', 'sw', 'se']:
        return chars
    else: 
        return chars[0]

def find_tile(tile_line): 
    coord = (0,0,0)
    line_parse = tile_line
    while len(line_parse) > 0: 
        direction = direction_split(line_parse[0:2])
        coord = dir_add_hex(direction, coord)        
        line_parse = line_parse[len(direction):]
    return coord 
# %%
flip_list = []
for tile_line in tile_directions: 
    flip_tile = find_tile(tile_line)
    if flip_tile not in flip_list: 
        flip_list.append(flip_tile)
    else: 
        flip_list.remove(flip_tile)

# %%
# part 1 answer
len(flip_list)
# %%
