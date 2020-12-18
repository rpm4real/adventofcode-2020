#%%
import re 
with open('input.txt') as file: 
    math_lines = file.read().split('\n') 
#%% 

def op_convert(op_string): 
    """convert operator character to lambda function"""
    if op_string == '*': 
        return lambda x,y: x*y 
    elif op_string == '+':
        return lambda x,y: x+y

def split_chunk(chunk): 
    """separate an expression into first operand, operation, and rest as tuple"""
    chunk = chunk.strip()
    for op_match in re.finditer('\+|\*', chunk): 
        first_chunk = chunk[0:op_match.start()]
        if first_chunk.count('(') == first_chunk.count(')'): 
            break 
    if first_chunk.count('(') != first_chunk.count(')'): 
        # in case of outer nesting, re-run without paren
        return split_chunk(chunk[1:-1])
    return first_chunk, op_convert(op_match[0]), chunk[op_match.end():]

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def run_chunk(chunk): 
    """run a chunk in a reduce-like format """
    if is_int(chunk):
        return int(chunk)
    else: 
        operand, op, rest = split_chunk(chunk)
        return op( run_chunk(operand), run_chunk(rest) )

# %%
totals = 0
for line in math_lines: 
    totals += run_chunk(line[::-1])

print(totals)
# %%
