import random

# Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck =[], num_cards=1):
        drawn_cards = deck.deal(num_cards)
        self.cards.extend(drawn_cards)
        return drawn_cards

    def discard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            print("Card not in hand.")
            return None

    def receive_cards(self, cards = []):
        self.cards.extend(cards)

# Define the Deck class
class Deck:
    def __init__(self, suits =  [], values = []):

     #  for suit in suits:
     #     for value in values:
     #         self.cards.append(Card(suit,value))

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def deal(self, num_cards):
        dealt_cards = random.sample(self.cards, num_cards)
        self.cards = [card for card in self.cards if card not in dealt_cards]
        return dealt_cards

    def draw(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

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

# Example usage:
spanish_deck = SpanishDeck()
english_deck = EnglishDeck()
player_hand = Hand()

player_hand.draw(spanish_deck, 3)
player_hand.discard(player_hand.cards[0])
player_hand.receive_cards(english_deck.deal(2))
spanish_deck.shuffle()
card_drawn = spanish_deck.draw()
print(card_drawn)
