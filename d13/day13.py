#%% 
import math 
with open('input.txt') as file: 
    lines = file.read().split('\n')
timestamp = int(lines[0])
bus_ids = [int(x) for x in lines[1].split(',') if x != 'x']
# %%

wait_times = [math.ceil(timestamp/float(id))*id - timestamp for id in bus_ids]
min_wait = min(wait_times)
bus_id = bus_ids[wait_times.index(min_wait)]

print(min_wait, bus_id, min_wait*bus_id)
# %%
