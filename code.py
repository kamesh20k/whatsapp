# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,15),['Spade','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got this:")
for i in range(6):
   print(deck[i][0], "of", deck[i][1])
