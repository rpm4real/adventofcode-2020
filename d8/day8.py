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

def run_lines(program):
    """run all lines until termination or loop reached.
    Returns acc and boolean (false if infinite loop)"""
    next_line = 0 
    acc = 0
    line_list = []
    while next_line not in line_list and next_line < len(program):
        line_list.append(next_line)
        current_line = next_line
        acc, next_line = exec_line(program[current_line], current_line, acc)
    return acc, next_line == len(program)
#%% 
# part 1
run_lines(logic)

# %%
