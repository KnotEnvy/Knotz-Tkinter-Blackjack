# Knotz Card Games

This is a card game project that includes several classic card games, such as Knotz Blackjack, Knotz War, and Knotz 5 Card. You can play these games online with other players or against the computer. The project is written in Python and uses the Pygame library for graphics and sound.

## Features

- Three different card games to choose from: Knotz Blackjack, Knotz War, and Knotz 5 Card.
- Offline single-player mode that lets you play against the computer with adjustable difficulty levels.
- Customizable card decks and backgrounds that you can unlock by earning coins and achievements. (added in time)
- Leaderboards and statistics that track your performance and progress. (added in time)

## Installation

To run this project, you need to have Python 3 and Pygame installed on your system. You can download them from the following links:

- [Python 3](https://www.python.org/downloads/)
- [Pygame](https://www.pygame.org/download.shtml)

After installing Python and Pygame, you can clone this repository or download the zip file and extract it. Then, navigate to the project folder and run the main.py file:

```bash
cd knotz-card-games
python main.py
```

## How to Play

When you launch the game, you will see the main menu where you can choose which game mode and which card game you want to play. You can also access the settings, the shop, the leaderboards, and the help menu from here.

### Knotz Blackjack

The goal of this game is to get as close to 21 as possible without going over. You start with two cards and can choose to hit (get another card) or stand (stop getting cards). The dealer will also get two cards, one of which is hidden. If you get 21 with your first two cards, you have a blackjack and win automatically. If you go over 21, you bust and lose. If neither you nor the dealer busts, the one with the higher total wins. If both have the same total, it's a tie.

### Knotz War

The goal of this game is to win all the cards from your opponent. You start with half of the deck and your opponent gets the other half. Each round, both players reveal the top card of their pile and compare them. The player with the higher card wins both cards and puts them at the bottom of their pile. If both cards have the same value, it's a war. In a war, both players put three cards face down and one card face up. The player with the higher face-up card wins all the cards. If both face-up cards are equal, another war occurs. The game ends when one player has no cards left.

### Knotz 5 Card

The goal of this game is to have a better poker hand than your opponent. You start with five cards and can choose to discard up to three cards and get new ones. Your opponent does the same. Then, both players reveal their hands and compare them. The player with the higher hand wins. The ranking of poker hands is as follows:

- Royal flush: A, K, Q, J, 10 of the same suit
- Straight flush: Five consecutive cards of the same suit
- Four of a kind: Four cards of the same value
- Full house: Three of a kind and a pair
- Flush: Five cards of the same suit
- Straight: Five consecutive cards of different suits
- Three of a kind: Three cards of the same value
- Two pair: Two pairs of different values
- One pair: Two cards of the same value
- High card: The highest card in your hand

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by multiple tutorials on how to make a blackjack games in Python.

The card images are included in the project.

The background images are included in the project.

The sound effects are included in the project.
