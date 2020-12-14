#%%
with open('input.txt') as file: 
    rules = file.read().split('\n')

# %%
#part 1 
possible_bag_list = ['shiny gold']
for bag in possible_bag_list: 
    for rule in rules: 
        outer, inners = rule.split('contain')
        if bag in inners and outer not in possible_bag_list: 
            possible_bag_list.append(outer.replace('bags ',''))

bag_set = set(possible_bag_list)
len(bag_set)-1
# %%
#part 2 

def find_bag_rule(bag_name): 
    for rule in rules: 
        rule_def = rule.split('contain ')
        if bag_name.strip(' ') in rule_def[0]: 
            return rule_def[1]
    print('cannot find {0}'.format(bag_name))

def cnt_bags(bag_name): 
    rule_def = find_bag_rule(bag_name)
    if 'no other bags' in rule_def: 
        return 0
    else: 
        containing_bags = 0
        inside_bags = rule_def.split(', ')
        for inside_bag_rule in inside_bags: 
            num, bag = inside_bag_rule[0], inside_bag_rule[1:].strip('.s')
            containing_bags += int(num) + int(num)*cnt_bags(bag)
        return containing_bags


# %%
cnt_bags('shiny gold bags')  
# %%
