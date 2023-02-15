import random
from definitions import face_cards

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        if value in face_cards:
            value_true = face_cards[value]
        else:
            value_true = value

        self.value_true = value_true

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        dealt = self.cards[0]
        self.cards = self.cards[1:]
        return dealt
