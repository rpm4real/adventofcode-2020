#%% 
pub_key1 = 15733400
#pub_key1 = 5764801 #DEBUG 
pub_key2 = 6408062

starting_subject = 7 
subject = starting_subject 
#BRUTE FORCE! 
for n in range(0,10000000): 
    subject *= 7
    subject = subject % 20201227
    #print(subject)
    if subject == pub_key1: 
        print('found key 1, loop size: ', n)
        break
    elif subject == pub_key2: 
        print('found key 2, loop size: ', n)
        break
# %%
#found loop size for key 1 
key1_loop_size = n + 2 
# %%
def get_transformed(val, N): 
    new_val = 1 
    for k in range(N): 
        new_val *= val 
        new_val = new_val % 20201227
        #print(k, new_val)
    return new_val 
# %%
get_transformed(7, key1_loop_size)

#%% 
get_transformed(pub_key2, key1_loop_size)
# %%
