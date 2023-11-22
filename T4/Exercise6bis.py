import random

# Define the Card class
class Card:
    def __init__(self, suit = str, value = str):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck, num_cards=1) -> []:
        drawn_cards = deck.deal(num_cards)
        self.cards.extend(drawn_cards)
        return drawn_cards

    def discard(self, card = Card) -> Card:
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            print("Card not in hand.")
            return None

    def receive_cards(self, cards = []) -> None:
        self.cards.append(cards)
        self.cards.extend(cards) <...

# Define the Deck class
class Deck:
    def __init__(self, suits = [], values = []):
       # TODO

    def deal(self, num_cards = int):
        # TODO

    def draw(self) -> Card:
        # TODO

    def shuffle(self) -> None:
        # TODO

# Define the SpanishDeck class
class SpanishDeck(Deck):
    def __init__(self):
        suits = ['Coins', 'Cups', 'Swords', 'Clubs']
        values = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        super().__init__(suits, values)

# Define the EnglishDeck class
class EnglishDeck(Deck):
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        super().__init__(suits, values)