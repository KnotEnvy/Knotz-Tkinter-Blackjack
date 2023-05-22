from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title('CardDeck')
# root.iconbitmap
root.geometry("1200x800")
root.configure(background="green")

#test for 21
def blackjack_shuffle(player):
    if player == "dealer":
        if len(dscore) == 2:
            if dscore[0] + dscore[1] == 21:
                messagebox.showinfo("Dealer Wins!", "Blackjack! Dealer Wins!!")
                #disable buttons
                card_button.config(state="disabled")
                stand_button.config(state="disabled")

    if player == "player":
        if len(pscore) == 2:
            if pscore[0] + pscore[1] == 21:
                messagebox.showinfo("You Won!", "Blackjack! You Win!!")
                #disable buttons
                card_button.config(state="disabled")
                stand_button.config(state="disabled")



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
    #enable buttons
    card_button.config(state="normal")
    stand_button.config(state="normal")
    #clear all old cards from previous hands
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(F'{value}_of_{suit}')

    #create players
    global dealer, player, dealer_spot, player_spot, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []
    dealer_spot = 0
    player_spot = 0

    #shuffle 2 cards for player and dealer
    player_hit()
    player_hit()
    dealer_hit()
    dealer_hit()


    #put number of remaining in title bar
    root.title(f'CardDeck - {len(deck)} Cards Left')

def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            #get dealer card
            #grab a random card dealer
            dealer_card = random.choice(deck)
            #remove from deck
            deck.remove(dealer_card)
            #append to dealer list
            dealer.append(dealer_card)
            #append to dealer score
            dcard = int(dealer_card.split("_", 1)[0])
            if dcard == 14:
                dscore.append(11)
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dscore.append(10)
            else:
                dscore.append(dcard)



            #output card to screen
            global dealer_image1,dealer_image2,dealer_image3,dealer_image4,dealer_image5

            if dealer_spot == 0:
                dealer_image1 = resize_cards(f'images/cards/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image1)
                #increment dealer spot
                dealer_spot += 1
            elif dealer_spot == 1:
                dealer_image2 = resize_cards(f'images/cards/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image2)
                #increment dealer spot
                dealer_spot += 1
            elif dealer_spot == 2:
                dealer_image3 = resize_cards(f'images/cards/{dealer_card}.png')
                dealer_label_3.config(image=dealer_image3)
                #increment dealer spot
                dealer_spot += 1
            elif dealer_spot == 3:
                dealer_image4 = resize_cards(f'images/cards/{dealer_card}.png')
                dealer_label_4.config(image=dealer_image4)
                #increment dealer spot
                dealer_spot += 1
            elif dealer_spot == 4:
                dealer_image5 = resize_cards(f'images/cards/{dealer_card}.png')
                dealer_label_5.config(image=dealer_image5)
                #increment dealer spot
                dealer_spot += 1
            

            root.title(f'CardDeck - {len(deck)} Cards Left')
        except:
            root.title(f'CardDeck - No Cards Left Kracka!!')

        blackjack_shuffle("dealer")

def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            #get player card
            #grab a random card player
            player_card = random.choice(deck)
            #remove from deck
            deck.remove(player_card)
            #append to dealer list
            player.append(player_card)
            #output card to screen
            #append to dealer score
            pcard = int(player_card.split("_", 1)[0])
            if pcard == 14:
                pscore.append(11)
            elif pcard == 11 or pcard == 12 or pcard == 13:
                pscore.append(10)
            else:
                pscore.append(pcard)

            global player_image1,player_image2,player_image3,player_image4,player_image5

            if player_spot == 0:
                player_image1 = resize_cards(f'images/cards/{player_card}.png')
                player_label_1.config(image=player_image1)
                #increment player spot
                player_spot += 1
            elif player_spot == 1:
                player_image2 = resize_cards(f'images/cards/{player_card}.png')
                player_label_2.config(image=player_image2)
                #increment player spot
                player_spot += 1
            elif player_spot == 2:
                player_image3 = resize_cards(f'images/cards/{player_card}.png')
                player_label_3.config(image=player_image3)
                #increment player spot
                player_spot += 1
            elif player_spot == 3:
                player_image4 = resize_cards(f'images/cards/{player_card}.png')
                player_label_4.config(image=player_image4)
                #increment player spot
                player_spot += 1
            elif player_spot == 4:
                player_image5 = resize_cards(f'images/cards/{player_card}.png')
                player_label_5.config(image=player_image5)
                #increment player spot
                player_spot += 1
            

            root.title(f'CardDeck - {len(deck)} Cards Left')
        except:
            root.title(f'CardDeck - No Cards Left Kracka!!')

        blackjack_shuffle("player")



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
        dealer_label_1.config(image=dealer_image)
       

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
        player_label_1.config(image=player_image)
        

        root.title(f'CardDeck - {len(deck)} Cards Left')


    except:
        root.title(f'CardDeck - No Cards Left Kracka!!')

my_frame= Frame(root, bg="green")
my_frame.pack(pady=20)

#create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

#put dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

#put player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

#create frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

#create a couple buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)                        

card_button = Button(button_frame, text="Hit me Homie!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stay Homie!",font=("Helvetica", 14)) 
stand_button.grid(row=0, column=2)

shuffle()

root.mainloop()