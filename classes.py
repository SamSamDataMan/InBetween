import random
from definitions import face_cards, values, suits

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.value_true = face_cards.get(value, value)

class Deck:
    def __init__(self):
        self.cards = self.generate_cards()
        self.shuffle()

    def generate_cards(self):
        cards = []
        for suit in suits:
            for value in values:
                cards.append(Card(face_cards.get(value, value), suit))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        dealt = self.cards[0]
        self.cards = self.cards[1:]
        return dealt

class Dealer:
    def __init__(self):
        pass

    def greeting(self):
        greeting = random.choice(['Changing $600!',
                                  'You don\'t know when to quit, do ya Griswold?',
                                  'Why don\'t you give me half the money your were gonna bet, then we\'ll go out back, I\'ll kick you in the nuts, and we\'ll call it a day!',
                                  'Big bet for a BIG man... Sure you don\'t want to save a few bucks for the buffet?',
                                  ])
        print('')
        print(greeting)
        print('')

    def dialogue_winner(self):
        winner_message = random.choice(['18, 27, 35... dealer busts! Looks like you all win again!',
                                        'Winner, winner - Crisp dinner!',
                                        'Winner! Now go celebrate with a round of frosty chocolate milkshakes!',
                                        'You\'ve won, but at what cost?'
                                        ])

        print('')
        print(winner_message)
        print('')

    def dialogue_loser(self):
        loser_message = random.choice(['You lose, stanger',
                                       'You tried your best, and you failed miserably. The lesson is: Never try.',
                                       'You get nothing! You lose! Good day sir! ',
                                       'You\'ve lost is all. You got greedy, Martin.',
                                       '... And it\'s gone!',
                                       ])

        print(loser_message)
        print('')
