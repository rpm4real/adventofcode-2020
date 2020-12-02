#%%
with open('d1/input.txt') as file: 
    nums = file.read().split('\n')

nums = list(map(int, nums))

# get two numbers that sum to 2020 in input.txt 
#%% 
for j in range(1010): 
    k = 2020-j 
    if k in nums and j in nums: 
        print(j,k,j*k)
        break

#%% 
# get three numbers that sum to 2020 
from itertools import combinations
from functools import reduce
comb_num = 3
my_combs = combinations(nums,comb_num)
for comb in my_combs: 
    if sum(comb) == 2020: 
        print(comb, reduce(lambda x,y: x*y,comb))
        break

