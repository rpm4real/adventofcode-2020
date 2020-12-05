#%%
import re 
with open('input.txt') as file: 
    pass_file = file.read().split('\n\n')

parse1 = [re.split('\s', p) for p in pass_file]




#%%
pass_list = []
for passport in parse1: 
    mydict = {}
    for field in passport: 
        fields = field.split(':')
        mydict[fields[0]] = fields[1]
    pass_list.append(mydict)

# %%

pass_cnt = 0 
for passport in pass_list: 
    if len(passport) == 8: 
        pass_cnt += 1 
    elif len(passport) == 7 and 'cid' not in passport:   
        pass_cnt +=1 

print(pass_cnt)
# %%

# def hgt(x): 
#     a = re.findall('cm|in',x)[0]
#     b = re.split(a, x)[0]
#     lookup = {
#         'cm': lambda x: x in range(150,194),
#         'in': lambda x: x in range(59,77)
#     }
#     return lookup.get(a,False)(int(b))

# # %% 
# 'byr': lambda x: int(x) in range(1920,2003), 
# 'iyr': lambda x: int(x) in range(2010,2021), 
# 'eyr': lambda x: int(x) in range(2020,2031), 
# 'hgt': hgt, 
# 'hcl': 

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.