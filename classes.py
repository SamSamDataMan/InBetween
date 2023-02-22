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
