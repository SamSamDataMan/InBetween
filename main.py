import random
from classes import Deck, Dealer

deck = Deck()
dealer = Dealer()

dealer.greeting()

a = deck.deal()  # deal first board card
b = deck.deal()  # deal second board card

a, b = dealer.swap_board(a, b)

dealer.print_board(a, b)

if a.value_true == b.value_true or b.value_true - a.value_true == 1:  # auto-lose conditions
    dealer.dialogue_loser()
else:
    action = dealer.take_wagers()
    if action == 'fold':
        dealer.dialogue_loser()
    if action == 'bet':
        c = deck.deal()
        dealer.print_board_result(a, b, c)
