# 1.The game starts with certain initial amount of dollars.

# 2.At each round of the game, instead of flipping a coin,
# the player shuffles a deck and draws 6 cards. If the drawn
# hand contains at least one ace, the player gains a dollar,
# otherwise they lose a dollar.

# 3.The game runs until the player either runs out of money or
# doubles their initial amount.
import random

faceValues = ['ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'jack',
              'queen', 'king']

suits = ['clubs', 'diamonds', 'hearts',
         'spades']

def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]

def suitOf(card):
    return card.split()[2]
deck = shuffledDeck()

while True:
    initial = int(input('Enter initial amount: '))
    balance = initial
    
    roundsPlayed = 0
    keeplaying=True
    gamePlayed = 0
    
    while keeplaying:
        if (gamePlayed == 1000):
            keeplaying = False
        deck = shuffledDeck()
        cards = [deck[0],deck[1],deck[2],deck[3],deck[4],deck[5]]
        won = False
        for card in cards:
            if faceValueOf(card) == 'ace':
                won = True
        if(won):
            balance+=1
        else:
            balance-=1
        roundsPlayed+=1
        if balance == 0:
            balance = initial
            gamePlayed += 1
    print('Average number of rounds: ',roundsPlayed/gamePlayed)
