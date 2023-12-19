import random

# Define la clase Card
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

# Define la clase Hand
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck =[], num_cards=1):
        # Dibuja cartas del mazo y las agrega a la mano
        drawn_cards = deck.deal(num_cards)
        self.cards.extend(drawn_cards)
        return drawn_cards
    
    #El método draw simula el acto de dibujar cartas de un mazo y añadirlas a la mano.
    #Toma dos argumentos: deck, que es el mazo del cual se están dibujando las cartas (por defecto es una lista vacía)
    # y num_cards, que es el número de cartas que se quieren dibujar (por defecto es 1).
    #deck.deal(num_cards): Este llamado a método utiliza el mazo (deck) para extraer un número específico de cartas (num_cards) mediante el método deal del mazo.
    #Este método debería existir en el mazo y debería devolver una lista de cartas.
    #self.cards.extend(drawn_cards): Agrega las cartas dibujadas a la lista de cartas en la mano (self.cards).
    #extend se utiliza para añadir múltiples elementos al final de la lista.
    #return drawn_cards: Devuelve la lista de cartas dibujadas.

    def discard(self, card):
        # Descarta una carta de la mano
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            print("Card not in hand.")
            return None

    def receive_cards(self, cards = []):
        # Recibe cartas y las agrega a la mano
        self.cards.extend(cards)

# Define la clase Deck
class Deck:
    def __init__(self, suits =  [], values = []):

        # Inicializa el mazo con cartas
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def deal(self, num_cards):
        # Reparte un número específico de cartas al azar del mazo
        dealt_cards = random.sample(self.cards, num_cards)
        self.cards = [card for card in self.cards if card not in dealt_cards]
        return dealt_cards

    def draw(self):
        # Extrae la primera carta del mazo
        return self.cards.pop(0)

    def shuffle(self):
        # Baraja el mazo
        random.shuffle(self.cards)

# Define la clase SpanishDeck que hereda de Deck
class SpanishDeck(Deck):
    def __init__(self):
        suits = ['Coins', 'Cups', 'Swords', 'Clubs']
        values = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        super().__init__(suits, values)

# Define la clase EnglishDeck que hereda de Deck
class EnglishDeck(Deck):
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        super().__init__(suits, values)

# Uso de ejemplo:
spanish_deck = SpanishDeck()
english_deck = EnglishDeck()
player_hand = Hand()

# Dibuja cartas del mazo español a la mano del jugador
player_hand.draw(spanish_deck, 3)
# Descarta la primera carta de la mano
player_hand.discard(player_hand.cards[0])
# Recibe 2 cartas del mazo inglés y las agrega a la mano
player_hand.receive_cards(english_deck.deal(2))
# Baraja el mazo español
spanish_deck.shuffle()
# Extrae la primera carta del mazo español
card_drawn = spanish_deck.draw()
print(card_drawn)
