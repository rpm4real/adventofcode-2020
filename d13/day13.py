#%% 
import math 
with open('input.txt') as file: 
    lines = file.read().split('\n')
timestamp = int(lines[0])
bus_ids = [int(x) for x in lines[1].split(',') if x != 'x']
# %%
# part 1 
wait_times = [math.ceil(timestamp/float(id))*id - timestamp for id in bus_ids]
min_wait = min(wait_times)
bus_id = bus_ids[wait_times.index(min_wait)]

print(min_wait, bus_id, min_wait*bus_id)
# %%

#part 2 
bus_ids2 = [(lambda x: 1 if x=='x' else int(x))(x) for x in lines[1].split(',')]

# cheat sheet for visualing chinese remainders 
# base_ts = 17*x0
# base_ts = 37*x1 - 11
# base_ts = 409*x2 - 17
# base_ts = 29*x3 - 19


#%% 
from functools import reduce 
def chinese_remainder(n, a):
    sums = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sums += a_i * mul_inv(p, n_i) * p
    return sums % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# %%
bus_n = [b for b in bus_ids2 if b > 1]
a_n = [- bus_ids2.index(val) for val in bus_n]
result = chinese_remainder(bus_n, a_n)

print(result)