#%% 
import pandas as pd
with open('input.txt') as file: 
    jolts = [int(x) for x in file.read().split('\n')]
jolt_df = pd.DataFrame(jolts, columns = ['joltage'])
# %%
jolt_df = jolt_df.sort_values(by = 'joltage')
jolt_df['prev_joltage'] = jolt_df['joltage'].shift(1)
jolt_df['jolt_diff'] = jolt_df['joltage'] - jolt_df['prev_joltage']
jolt_df.tail(10)

# %%
# part 1 answer
jolt_gaps = jolt_df.groupby('jolt_diff')['joltage'].count() + 1 #.product()
jolt_gaps.product()
# %%

