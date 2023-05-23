from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

SUITS = ["diamonds", "clubs", "hearts", "spades"]
VALUES = range(2, 15)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = f'{value}_of_{suit}.png'

    def score(self):
        if self.value == 14:
            return 11
        elif self.value in [11, 12, 13]:
            return 10
        else:
            return self.value

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, frame, name, game):
        self.frame = frame
        self.name = name
        self.game = game
        self.cards = []
        self.labels = [Label(self.frame, text='') for _ in range(5)]
        for i, label in enumerate(self.labels):
            label.grid(row=0, column=i, pady=20, padx=20)

    def hit(self, card):
        self.cards.append(card)
        self.update_images()

    def update_images(self):
        for i, card in enumerate(self.cards):
            image = self.game.resize_cards(f'images/cards/{card.image}')
            self.labels[i].config(image=image)

    def score(self):
        return sum(card.score() for card in self.cards)

class Game:
    def __init__(self, root):
        self.root = root
        self.deck = Deck()
        self.dealer = Player(LabelFrame(root, text="Dealer", bd=0), "Dealer", self)
        self.player = Player(LabelFrame(root, text="Player", bd=0), "Player", self)
        self.shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=self.shuffle)
        self.card_button = Button(root, text="Hit Me!", font=("Helvetica", 14), command=self.player_hit)
        self.stand_button = Button(root, text="Stand!", font=("Helvetica", 14), command=self.stand)

        self.shuffle_button.pack()
        self.card_button.pack()
        self.stand_button.pack()

    def deal_initial_cards(self):
        self.player.hit(self.deck.draw_card())
        self.player.hit(self.deck.draw_card())
        self.dealer.hit(self.deck.draw_card())
        self.dealer.hit(self.deck.draw_card())
    def resize_cards(self, card):
        # Open the image
        our_card_img = Image.open(card)

        # Resize The Image
        our_card_resize_image = our_card_img.resize((150, 218))
        
        # output the card
        global our_card_image
        our_card_image = ImageTk.PhotoImage(our_card_resize_image)

        # Return that card
        return our_card_image

    def shuffle(self):
        self.deck = Deck()
        self.dealer.cards = []
        self.player.cards = []
        self.dealer.update_images()
        self.player.update_images()
        self.root.title(f'Knotz Blackjack - {len(self.deck.cards)} Cards Left')

    def player_hit(self):
        if len(self.player.cards) < 5:
            self.player.hit(self.deck.draw_card())
            self.check_for_blackjack()

    def dealer_hit(self):
        if len(self.dealer.cards) < 5:
            self.dealer.hit(self.deck.draw_card())
            self.check_for_blackjack()

    def stand(self):
        while self.dealer.score() < 17:
            self.dealer_hit()
        self.check_for_winner()

    def check_for_blackjack(self):
        if len(self.player.cards) == 2 and self.player.score() == 21:
            messagebox.showinfo("Player Wins!", "Blackjack! Player Wins!")
        elif len(self.dealer.cards) == 2 and self.dealer.score() == 21:
            messagebox.showinfo("Dealer Wins!", "Blackjack! Dealer Wins!")

    def check_for_winner(self):
        if self.player.score() > 21:
            messagebox.showinfo("Player Busts!", f"Player Loses! {self.player.score()}")
        elif self.dealer.score() > 21:
            messagebox.showinfo("Dealer Busts!", f"Player Wins! {self.player.score()}")
        elif self.player.score() > self.dealer.score():
            messagebox.showinfo("Player Wins!", f"Player Wins! {self.player.score()}")
        elif self.dealer.score() > self.player.score():
            messagebox.showinfo("Dealer Wins!", f"Player Loses! {self.player.score()}")
        else:
            messagebox.showinfo("Push!", "It's a Tie!")


root = Tk()
root.title('Knotz Blackjack')
root.geometry("1200x800")
root.configure(background="green")

game = Game(root)
game.shuffle()

# Add dealer and player frames to the root window
game.dealer.frame.pack(padx=20, ipadx=20)
game.player.frame.pack(ipadx=20, pady=10)

# Add buttons to the root window
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

game.shuffle_button.grid(row=0, column=0, in_=button_frame)
game.card_button.grid(row=0, column=1, padx=10, in_=button_frame)
game.stand_button.grid(row=0, column=2, in_=button_frame)

# Deal initial cards
game.deal_initial_cards()

root.mainloop()

