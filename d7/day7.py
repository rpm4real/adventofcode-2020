#%%
with open('input.txt') as file: 
    rules = file.read().split('\n')

# %%
part 1 
target_bag = 'shiny gold'
possible_bag_list = ['shiny gold']
for bag in possible_bag_list: 
    for rule in rules: 
        outer, inners = rule.split('contain')
        if bag in inners and outer not in possible_bag_list: 
            possible_bag_list.append(outer.replace('bags ',''))

bag_set = set(possible_bag_list)

# %%
len(bag_set)
# %%
#part 2 