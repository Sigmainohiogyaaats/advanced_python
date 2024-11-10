import random, itertools 

card_deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))

random.shuffle(card_deck) 
#print(card_deck)

print('Your cards are: ') 
for i in range(5): 
    print(card_deck[i][0], 'of', card_deck[i][1])