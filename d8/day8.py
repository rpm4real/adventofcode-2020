#%% 
with open('input.txt') as file: 
    logic = file.read().split('\n')

def exec_line(line,line_num,acc): 
    """return accumulator and next line num"""
    instr, val = line.split(' ')
    return {
        'nop': [acc, line_num+1],
        'acc': [acc+int(val), line_num+1],
        'jmp': [acc, line_num+int(val)]
    }.get(instr)

#%% 
next_line = 0 
acc = 0
line_list = []
while next_line not in line_list:
    line_list.append(next_line)
    current_line = next_line
    acc, next_line = exec_line(logic[current_line], current_line, acc)
print(acc)
# %%
