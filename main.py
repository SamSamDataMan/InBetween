import random

######
# Likely moving this block to its own file
values = list(range(2, 15))
suits = ['clubs', 'diamonds', 'hearts', 'spades']

face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards(values, suits):
    cards = []
    for suit in suits:
        for value in values:
            if value in face_cards:
                card_value = face_cards[value]
                cards.append(Card(card_value, suit))
            else:
                cards.append(Card(value, suit))
    return cards

cards = generate_cards(values, suits)
############

random.shuffle(cards)

a = (cards[0].value, cards[0].suit)
b = (cards[1].value, cards[1].suit)

# assign value to face cards
if a[0] in face_cards:
    a_temp = face_cards[a[0]]
else:
    a_temp = a[0]
if b[0] in face_cards:
    b_temp = face_cards[b[0]]
else:
    b_temp = b[0]

# swap so lowest card is first
if a_temp > b_temp:
    a, a_temp, b, b_temp = b, b_temp, a, a_temp

print(a)
print(b)

if a_temp == b_temp or b_temp - a_temp == 1:
    print('You lose, loser!')
else:
    action = input('Bet or Fold?')
    counter = 0
    while action.lower() not in ('bet', 'fold'):
        if counter < 3:
            print('Try again, dummy')
        else:
            print('What are you, simple?')
        counter += 1
        action = input('Bet or Fold?')
    if action.lower() == 'fold':
        print('You lose, stanger')
    if action.lower() == 'bet':
        c = (cards[2].value, cards[2].suit)
        print(c)
        if c[0] in face_cards:
            c_temp = face_cards[c[0]]
        else:
            c_temp = c[0]
        if c_temp > a_temp and c_temp < b_temp:
            print('You win... bigly')
        else:
            print("You shouldnt'a did that... he's just a boy")
