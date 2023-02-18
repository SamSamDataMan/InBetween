import random
from classes import Card, Deck

deck = Deck()

a = deck.deal() # deal first board card
b = deck.deal() # deal second board card

if a.value_true > b.value_true: # swap so lowest card is shown first
    a, b = b, a

print(' - ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' - ') # print board

if a.value_true == b.value_true or b.value_true - a.value_true == 1: # auto-lose conditions
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
        c = deck.deal()
        if c.value_true > a.value_true and c.value_true < b.value_true:
            print(' - ' + str(a.value) + a.suit + ' ' + str(c.value) + c.suit + ' ' + str(b.value) + b.suit + ' - ')
            print('You win... bigly')
        elif c.value_true <= a.value_true:
            print(str(c.value) + c.suit + ' ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' - ')
            print("You shouldnt'a did that... he's just a boy")
        else:
            print(' - ' + str(a.value) + a.suit + ' - ' + str(b.value) + b.suit + ' ' + str(c.value) + c.suit)
            print('Oops... sorry')
