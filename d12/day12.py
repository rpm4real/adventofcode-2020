#%%
import cmath
from math import e, pi, radians
with open('input.txt') as file: 
    directions = [(line[0],int(line[1:])) for line in file.read().split('\n')]

#%% 

def rotation(change_dir, prev_orien): 
    rot = {'L': 1, 'R': -1}[change_dir[0]]
    new_orien = prev_orien*e**(1j*change_dir[1]*rot*pi/180)
    return complex(round(new_orien.real), round(new_orien.imag))

#%% 

coords = complex(0,0)
legend = {
    'N': complex(0,1),
    'S': complex(0,-1),
    'E': complex(1,0),
    'W': complex(-1,0)
}
orientation = complex(1,0)

for dir in directions: 
    if dir[0] in legend.keys(): 
        coords += dir[1]*legend[dir[0]]
    elif dir[0] == 'F': 
        coords += dir[1]*orientation
    elif dir[0] in ('L','R'):
        orientation = rotation(dir,orientation)
    
print(coords, abs(coords.real) + abs(coords.imag))


# %%
waypoint_loc = complex(10,1)
ship_loc = complex(0,0)

for dir in directions: 
    if dir[0] in legend.keys(): 
        waypoint_loc += dir[1]*legend[dir[0]]
    elif dir[0] == 'F': 
        ship_loc = ship_loc + dir[1]*waypoint_loc
    elif dir[0] in ('L','R'):
        waypoint_loc = rotation(dir,waypoint_loc)

print(ship_loc, abs(ship_loc.real) + abs(ship_loc.imag))

