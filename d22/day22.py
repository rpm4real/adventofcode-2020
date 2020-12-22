#%% 
with open('input.txt') as file: 
    hands = file.read().split('\n\n')

for k,hand in enumerate(hands): 
    hands[k] = [int(c) for c in hand.split('\n')[1:]]
p1_hand, p2_hand = hands
# %%
def sim_round(p1, p2): 
    round_cards = [p1.pop(0), p2.pop(0)]
    if sorted(round_cards) != round_cards: 
        return p1 + round_cards, p2 
    else: 
        return p1, p2 + sorted(round_cards)[::-1]
#%%
p1 = p1_hand.copy()
p2 = p2_hand.copy()
cnt = 0 
while len(p1) > 0 and len(p2) > 0:
    p1,p2 = sim_round(p1,p2)
    cnt += 1
# %%
# compute score (part 1 answer)
sum([card*mult for card, mult in zip(p1,reversed(range(1,len(p1)+1)))])

# %%
