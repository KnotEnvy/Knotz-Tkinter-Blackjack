from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Knotz Blackjack')
#root.iconbitmap
root.geometry("1200x800")
root.configure(background="green")

SUITS = ["diamonds", "clubs", "hearts", "spades"]
VALUES = range(2, 15)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_image_path(self):
        return f'images/cards/{self.value}_of_{self.suit}.png'

    def __str__(self):
        value_str = str(self.value) if self.value <= 10 else {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}[self.value]
        return f'{value_str} of {self.suit}'

class Player:
    def __init__(self):
        self.hands = [[]]
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)
        self.score += card.value

    @property
    def score(self):
        return [self.calculate_score(hand) for hand in self.hands]

    def calculate_score(self, hand):
        value = sum(card.value for card in hand)
        aces = sum(card.value == 14 for card in hand)  # 14 is the value of Ace in your code

        while value > 21 and aces:
            value -= 10  # Subtract 10 if Ace is counted as 11
            aces -= 1

        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class BlackjackGame:
    def __init__(self):
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = range(2, 15)
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.deck)
        self.player = Player()
        self.dealer = Player()
        self.insurance_bet = 0

    def deal_card(self, player):
        card = self.deck.pop()
        player.add_card(card)
        return card

    def player_hit(self):
        return self.deal_card(self.player)

    def dealer_hit(self):
        return self.deal_card(self.dealer)

    # ... rest of the game logic ...
    def player_turn(self):
        while True:
            action = self.player.decide_action()  # You need to implement this method in the Player class
            if action == "hit":
                self.player_hit()
                if self.player.score > 21:
                    return "bust"
            elif action == "stand":
                return "stand"

    def dealer_turn(self):
        while self.dealer.score < 17:
            self.dealer_hit()
        if self.dealer.score > 21:
            return "bust"
        else:
            return "stand"

    def compare_scores(self):
        if self.player.score > 21:
            return "dealer"
        elif self.dealer.score > 21:
            return "player"
        elif self.player.score > self.dealer.score:
            return "player"
        elif self.dealer.score > self.player.score:
            return "dealer"
        else:
            return "push"

    def play_round(self):
        player_result = self.player_turn()
        if player_result == "bust":
            return "dealer"
        dealer_result = self.dealer_turn()
        if dealer_result == "bust":
            return "player"
        return self.compare_scores()
    
    def double_down(self):
        if len(self.player.cards) > 2:
            raise Exception("You can only double down on your first two cards.")

        self.player_bet *= 2
        return self.player_hit()
    
    def split(self):
        if len(self.player.hands[0]) != 2 or self.player.hands[0][0].value != self.player.hands[0][1].value:
            raise Exception("You can only split a pair.")

        self.player.hands.append([self.player.hands[0].pop()])

        return self.player.hands
    
    def buy_insurance(self):
        if self.dealer.cards[0].value != 14:  # 14 is the value of Ace in your code
            raise Exception("You can only buy insurance when the dealer's up card is an Ace.")

        self.insurance_bet = self.player_bet / 2

        return self.insurance_bet
    
class BlackjackUI:
    def __init__(self, game):
        self.game = game
        self.root = Tk()
        self.root.title('Knotz Blackjack')
        self.root.geometry("1200x800")
        self.root.configure(background="green")

        # Add buttons for player actions
        self.hit_button = Button(self.root, text="Hit", command=self.game.player_hit)
        self.stand_button = Button(self.root, text="Stand", command=self.game.player_stand)
        self.double_down_button = Button(self.root, text="Double Down", command=self.game.double_down)
        self.split_button = Button(self.root, text="Split", command=self.game.split)
        self.buy_insurance_button = Button(self.root, text="Buy Insurance", command=self.game.buy_insurance)

        # Add labels to display the player's and dealer's hands
        self.player_hand_label = Label(self.root, text="")
        self.dealer_hand_label = Label(self.root, text="")

        # Place the widgets on the window
        self.hit_button.pack()
        self.stand_button.pack()
        self.double_down_button.pack()
        self.split_button.pack()
        self.buy_insurance_button.pack()
        self.player_hand_label.pack()
        self.dealer_hand_label.pack()

    def update_ui(self):
        # Update the UI based on the current game state
        self.player_hand_label['text'] = "Player's hand: " + str(self.game.player.cards)
        self.dealer_hand_label['text'] = "Dealer's hand: " + str(self.game.dealer.cards)

        # Enable or disable buttons based on the current game state
        self.double_down_button['state'] = 'normal' if len(self.game.player.cards) == 2 else 'disabled'
        self.split_button['state'] = 'normal' if len(self.game.player.cards) == 2 and self.game.player.cards[0].value == self.game.player.cards[1].value else 'disabled'
        self.buy_insurance_button['state'] = 'normal' if self.game.dealer.cards[0].value == 14 else 'disabled'

    def run(self):
        self.root.mainloop()


game = BlackjackGame()
ui =BlackjackUI(game)
ui.run()

root.mainloop()

