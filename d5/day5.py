#%%
import pandas as pd
with open('input.txt') as file: 
    board_list = file.read().split('\n')

#%% 
board_frame = pd.DataFrame(board_list, columns = ['code']) 

# %%

board_frame['row'] = board_frame['code'].str[:7]
board_frame['col'] = board_frame['code'].str[7:]

# %%
# function to do binary logic
def parse_code(code,bit1,bit0): 
    return 2**len(code) - int(code.replace(bit1,'1').replace(bit0,'0'),2)-1
# %%

#parse_code('FBFBBFF','F','B')
board_frame['row_val'] = board_frame['row'].apply(parse_code,args=('F','B'))
board_frame['col_val'] = board_frame['col'].apply(parse_code,args=('L','R'))
board_frame['seat_id'] = board_frame['row_val']*8 + board_frame['col_val']

board_frame['seat_id'].max()
# %%
