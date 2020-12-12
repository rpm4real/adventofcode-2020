#%%
import cmath
from math import e, pi, radians
with open('input.txt') as file: 
    directions = [(line[0],int(line[1:])) for line in file.read().split('\n')]

#%% 

def rotation(numb, degree): 
    if degree == 180 or degree == -180: 
        return numb*-1 
    elif degree == 90 
        return complex(numb.imag, numb.real)

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
    



# %%
