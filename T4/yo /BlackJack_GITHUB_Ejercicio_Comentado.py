import os  # Importa el módulo os para interactuar con el sistema de archivos.
from tkinter import PhotoImage, messagebox  # Importa clases de tkinter para imágenes y cuadros de mensajes.
import random  # Importa el módulo random para la generación de números aleatorios.
import tkinter as tk  # Importa tkinter con un alias para la creación de la interfaz gráfica de usuario.


# Clases para la lógica del juego
class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit  # El palo de la carta (corazones, diamantes, tréboles, picas).
        self.value = value  # El valor de la carta (2-10, J, Q, K, A).

    # Retorna el valor numérico de la carta para el juego de Blackjack.
    def get_numeric_value(self) -> int:
        if self.value in ['J', 'Q', 'K']:  # Las figuras valen 10.
            return 10
        elif self.value == 'A':  # El as vale 11 o 1, dependiendo de la mano.
            return 11
        else:  # Los números valen su propio valor.
            return int(self.value)

    def get_image(self):
        # Ruta absoluta al archivo de imagen
        path = r"C:\Users\usuario\OneDrive - Universidad Loyola Andalucía\Escritorio\bj_project-main\bj_project-main\img\{}_of_{}.png".format(self.value, self.suit)
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError(f"El archivo {path} no existe")

# Clase para representar un mazo de cartas.
class Deck:
    def __init__(self):
        self.cards = []  # Lista para almacenar las cartas del mazo.
        self.build()  # Llena el mazo con cartas al inicializar.
   
    # Crea un mazo de 52 cartas estándar.
    def build(self):
        for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))
    # Mezcla las cartas del mazo de forma aleatoria.
    def shuffle(self):
        random.shuffle(self.cards)
    # Reparte (elimina y retorna) la última carta del mazo.
    def deal(self) -> Card:
        return self.cards.pop()

# Clase para representar un mazo de cartas inglés, hereda de Deck y lo mezcla al iniciar.
class EnglishDeck(Deck):
    def __init__(self):
        super().__init__()  # Inicializa la clase base (Deck).
        self.shuffle()  # Mezcla las cartas tras inicializar el mazo.

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)
     # Calcula el valor total de la mano, ajustando el valor del as si es necesario.
    def value(self) -> int:
        total_value = 0
        ace_count = 0

        for card in self.cards:
            total_value += card.get_numeric_value()
            if card.value == 'A':
                ace_count += 1
        # Ajusta el valor del as si el total supera 21.
        while total_value > 21 and ace_count:
            total_value -= 10
            ace_count -= 1

        return total_value
# Clase para representar a un jugador en el juego.
class Player:
    def __init__(self, name):
        self.name = name # El nombre del jugador.
        self.hand = Hand()  # La mano del jugador.
# Clase principal que representa el juego de Blackjack.
class BlackjackGame:
     # Inicialización y métodos para gestionar el flujo del juego.
    def __init__(self):
        self.deck = EnglishDeck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def start_game(self):
        self.player.hand = Hand()
        self.dealer.hand = Hand()
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())

    def hit(self) -> bool:
        self.player.hand.add_card(self.deck.deal())
        return self.player.hand.value() <= 21

    def dealer_hit(self) -> bool:
        if self.dealer.hand.value() < 17:
            self.dealer.hand.add_card(self.deck.deal())
            return True
        return False

    def determine_winner(self):
        player_value = self.player.hand.value()
        dealer_value = self.dealer.hand.value()

        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21 or player_value > dealer_value:
            return f"{self.player.name} wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"
# Clase para la interfaz gráfica del juego de Blackjack.
class BlackjackGUI:
     # Inicialización y métodos para interactuar con la interfaz gráfica.
    def __init__(self, game):
        self.game = game

        self.root = tk.Tk()
        self.root.title("Blackjack")

        # Frames para el jugador y el crupier
        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(side=tk.LEFT, padx=10)

        self.deck_frame = tk.Frame(self.root)
        self.deck_frame.pack(side=tk.LEFT, padx=10)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(side=tk.RIGHT, padx=10)

        # Botón "Stand"
        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

        self.start_game()

    def start_game(self):
        self.game.start_game()
        self.update_interface()

    def handle_hit(self, event):
        if self.game.hit():
            self.update_interface()
        else:
            self.end_game("You've busted! The house wins.")

    def handle_stand(self):
        self.btn_stand.config(state=tk.DISABLED)
        while self.game.dealer_hit():
            self.update_interface()
        self.end_game(self.game.determine_winner())

    def update_interface(self):
        # Limpiar los widgets de los frames
        for frame in [self.player_frame, self.deck_frame, self.dealer_frame]:
            for widget in frame.winfo_children():
                widget.destroy()

        # Mostrar las cartas del jugador
        for card in self.game.player.hand.cards:
            img = PhotoImage(file=card.get_image())
            lbl = tk.Label(self.player_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.LEFT, padx=2)

        # Mostrar las cartas del crupier
        for card in self.game.dealer.hand.cards:
            img = PhotoImage(file=card.get_image())
            lbl = tk.Label(self.dealer_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.LEFT, padx=2)

        # Mostrar el mazo y el botón "Hit"
        deck_img = PhotoImage(file= r"C:\Users\usuario\OneDrive - Universidad Loyola Andalucía\Escritorio\bj_project-main\bj_project-main\img\card_back_01.png")
        deck_label = tk.Label(self.deck_frame, image=deck_img, cursor="hand2")
        deck_label.image = deck_img
        deck_label.pack(side=tk.TOP, padx=10)
        deck_label.bind("<Button-1>", self.handle_hit)

        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game_logic = BlackjackGame()  # Crea una instancia del juego.
    app = BlackjackGUI(game_logic)  # Crea una instancia de la interfaz gráfica del juego.
    app.run()  # Ejecuta la interfaz gráfica del juego.
