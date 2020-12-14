#%% 
from functools import reduce
with open('input.txt') as file: 
    program = file.read().split('\n')

def binary_convert(val): 
    return "{0:b}".format(int(val))

def mask_value(mask, val): 
    val = '0'*(36-len(val)) + val 
    return ''.join([m if m != 'X' else v for m,v in zip(mask,val)])

# %%
import re 
mem = {}
for line in program: 
    if line[0:4] == 'mask': 
        mask = line.split('= ')[1]
    else: 
        loc, val = line.split(' = ')
        address = re.search('\[(.*)\]',loc).group(1)
        bin_val = binary_convert(val)
        mem[address] = int(mask_value(mask,bin_val),2)

#%% 
sum(mem.values())