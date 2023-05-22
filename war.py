from tkinter import *
import random
from PIL import Image, ImageTk, ImageDraw



root = Tk()
root.title('KnotZ War')
# root.iconbitmap
root.geometry("1200x800")
root.configure(background="green")

# label = Label(root)
# label.pack()

# def display_fireworks():
#     particles = []

#     for _ in range(1000):
#         x = random.randint(0, 900)
#         y = random.randint(0, 550)
#         speed_x = random.uniform(-1, 1)
#         speed_y = random.uniform(-1, 1)
#         color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         particles.append([[x, y], [speed_x, speed_y], color])

#     def update_image(i):
#         if i < 60:
#             image = Image.new("RGB", (900, 550), "black")
#             draw = ImageDraw.Draw(image)

#             for particle in particles:
#                 position, speed, color = particle
#                 position[0] += speed[0]
#                 position[1] += speed[1]
#                 draw.ellipse((position[0]-2, position[1]-2, position[0]+2, position[1]+2), fill=color)

#             photo = ImageTk.PhotoImage(image)
#             label.config(image=photo)
#             label.image = photo

#             root.after(50, update_image, i+1)

#     update_image(0)

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
    global dealer, player, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []

    #grab a random card dealer
    dealer_card = random.choice(deck)
    #remove from deck
    deck.remove(dealer_card)
    #append to dealer list
    dealer.append(dealer_card)
    #output card to screen
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
    dealer_label.config(image=dealer_image)
    
    #grab a random card player
    player_card = random.choice(deck)
    #remove from deck
    deck.remove(player_card)
    #append to dealer list
    player.append(player_card)
    #output card to screen
    global player_image
    player_image = resize_cards(f'images/cards/{player_card}.png')
    player_label.config(image=player_image)


    #put number of remaining in title bar
    root.title(f'CardDeck - {len(deck)} Cards Left')

    #get score
    score(dealer_card, player_card)
    


#deal cards out
def deal_cards():
    try:
        #get dealer card
        #grab a random card dealer
        dealer_card = random.choice(deck)
        #remove from deck
        deck.remove(dealer_card)
        #append to dealer list
        dealer.append(dealer_card)
        #output card to screen
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
        dealer_label.config(image=dealer_image)

        #get player card
        #grab a random card player
        player_card = random.choice(deck)
        #remove from deck
        deck.remove(player_card)
        #append to dealer list
        player.append(player_card)
        #output card to screen
        global player_image
        player_image = resize_cards(f'images/cards/{player_card}.png')
        player_label.config(image=player_image)

        root.title(f'CardDeck - {len(deck)} Cards Left')
        score(dealer_card, player_card)

    except:
        if dscore.count("x") == pscore.count("x"):
            root.title(f'CardDeck - No Cards Left Kracka! Tie! {dscore.count("x")} to {pscore.count("x")}')
        elif dscore.count("x") > pscore.count("x"):
            root.title(f'CardDeck - No Cards Left Kracka! Dealer Wins! {dscore.count("x")} to {pscore.count("x")}')
        else: 
            root.title(f'CardDeck - No Cards Left Kracka! You Win! {pscore.count("x")} to {dscore.count("x")}')

def score(dealer_card, player_card):
    #spit number from suits
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])
    

    #compare numbers for war winner
    if dealer_card == player_card:
        score_label.config(text="Tie! Play again sucka!!")
        
    elif dealer_card > player_card:
        score_label.config(text="You Lose Fool!!")
        dscore.append("x")
    else:
        score_label.config(text="Dats What I'm Saying!!")
        #display_fireworks()
        pscore.append("x")

    root.title(f'CardDeck - {len(deck)} Cards Left |   Dealer : {dscore.count("x")} vs. Player: {pscore.count("x")}')

def on_enter(event):
    r = random.randint(0, 150)
    g = random.randint(0, 150)
    b = random.randint(0, 150)
    color = f'#{r:02x}{g:02x}{b:02x}'
    event.widget.config(bg=color)

def on_leave(event):
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    event.widget.config(bg=color)




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

player_label = Label(player_frame, text=("Times New Roman", 14))
player_label.pack(pady=20)

#score label
score_label = Label(root, text="", font=("Times New Roman", 14), bg="green")
score_label.pack(pady=20)

#create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Times New Roman", 14), command=shuffle, borderwidth=5, relief='raised')
shuffle_button.pack(pady=20)                        
card_button = Button(root, text="Get Cards", font=("Times New Roman", 14), command=deal_cards, borderwidth=5, relief='raised')
card_button.pack(pady=20)

shuffle_button.bind("<Enter>", on_enter)
shuffle_button.bind("<Leave>", on_leave)

card_button.bind("<Enter>", on_enter)
card_button.bind("<Leave>", on_leave)
shuffle()

root.mainloop()