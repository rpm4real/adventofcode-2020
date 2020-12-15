#%% 
from functools import reduce
with open('input.txt') as file: 
    program = file.read().split('\n')

def binary_convert(val): 
    return "{0:b}".format(int(val))

def mask_value(mask, val): 
    val = val.zfill(36)
    return ''.join([m if m != 'X' else v for m,v in zip(mask,val)])

def mask_address(mask, address): 
    address = address.zfill(36)
    masked = ''
    for m,a in zip(mask,address): 
        if m == '0': 
            masked += a
        elif m == '1': 
            masked += '1'
        else: 
            masked += 'X'
    return masked 

def masked_address_cases(masked_address): 
    float_chars = masked_address.count('X')
    address_list = []
    for k in range(2**float_chars): 
        bin_replace = list(binary_convert(k).zfill(float_chars))
        f = lambda x: bin_replace.pop() if x=='X' else x
        address_list.append(int(''.join([f(b) for b in masked_address]),2))
    return address_list
        


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

#%% 
# part 2 
import re 
mem = {}
for line in program: 
    if line[0:4] == 'mask': 
        mask = line.split('= ')[1]
    else: 
        loc, val = line.split(' = ')
        address = re.search('\[(.*)\]',loc).group(1)
        bin_address = binary_convert(address)
        masked_address = mask_address(mask, bin_address)
        for case in masked_address_cases(masked_address): 
            mem[case] = int(val)
sum(mem.values())

