import random
from definitions import face_cards, values, suits

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
    def __init__(self):
        self.cards = self.generate_cards(values, suits)
        self.shuffle()

    def generate_cards(self, values, suits):
        cards = []
        for suit in suits:
            for value in values:
                if value in face_cards:
                    card_value = face_cards[value]
                    cards.append(Card(card_value, suit))
                else:
                    cards.append(Card(value, suit))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        dealt = self.cards[0]
        self.cards = self.cards[1:]
        return dealt
