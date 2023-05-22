from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title('CardDeck')
# root.iconbitmap
root.geometry("900x500")
root.configure(background="green")

#resize cards
def resize_cards(card):
    #open image
    our_card_img = Image.open(card)

    #resize image
    our_card_resize_image = our_card_img.resize((150,218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    # return that card
    return our_card_image


#shuffle the cards
def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(F'{value}_of_{suit}')

    #create players
    global dealer, player
    dealer = []
    player = []

    #grab a random card dealer
    card = random.choice(deck)
    #remove from deck
    deck.remove(card)
    #append to dealer list
    dealer.append(card)
    #output card to screen
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{card}.png')
    dealer_label.config(image=dealer_image)
    
    #grab a random card player
    card = random.choice(deck)
    #remove from deck
    deck.remove(card)
    #append to dealer list
    player.append(card)
    #output card to screen
    global pkayer_image
    player_image = resize_cards(f'images/cards/{card}.png')
    player_label.config(image=player_image)


    #put number of remaining in title bar
    root.title(f'CardDeck - {len(deck)} Cards Left')

#deal cards out
def deal_cards():
    try:
        #get dealer card
        #grab a random card dealer
        card = random.choice(deck)
        #remove from deck
        deck.remove(card)
        #append to dealer list
        dealer.append(card)
        #output card to screen
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{card}.png')
        dealer_label.config(image=dealer_image)
       

        #get player card
        #grab a random card player
        card = random.choice(deck)
        #remove from deck
        deck.remove(card)
        #append to dealer list
        player.append(card)
        #output card to screen
        global player_image
        player_image = resize_cards(f'images/cards/{card}.png')
        player_label.config(image=player_image)
        

        root.title(f'CardDeck - {len(deck)} Cards Left')


    except:
        root.title(f'CardDeck - No Cards Left Kracka!!')

my_frame= Frame(root, bg="green")
my_frame.pack(pady=20)

#create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

#put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

#create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)                        

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)

shuffle()

root.mainloop()