#%% 
input = [1,12,0,20,8,16]
number_tracker = {}
turn_cnt = 1 
for num in input: 
    number_tracker[num] = turn_cnt 
    turn_cnt += 1
    prev_num = num  

while turn_cnt <= 2020: #part 2, 30000000 instead
    if prev_num in number_tracker: 
        new_num = turn_cnt - 1 - number_tracker[prev_num] 
    else: 
        new_num = 0
    number_tracker[prev_num] = turn_cnt-1 #set previous number
    turn_cnt +=1 
    prev_num = new_num 

print(prev_num)


