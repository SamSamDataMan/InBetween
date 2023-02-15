import random
from classes import Card, Deck
from definitions import values, suits, face_cards

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

deck = Deck(cards)

deck.shuffle(cards)

a = cards[0]
b = cards[1]

# swap so lowest card is first
if a.value_true > b.value_true:
    a, b = b, a

print(' - ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' - ')

if a.value_true == b.value_true or b.value_true - a.value_true == 1:
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
        c = cards[2]
        if c.value_true > a.value_true and c.value_true < b.value_true:
            print(' - ' + str(a.value) + a.suit + ' ' + str(c.value) + c.suit + ' ' + str(b.value) + b.suit + ' - ')
            print('You win... bigly')
        elif c.value_true <= a.value_true:
            print(str(c.value) + c.suit + ' ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' - ')
            print("You shouldnt'a did that... he's just a boy")
        else:
            print(' - ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' ' + str(c.value) + c.suit)
            print('Oops... sorry')
