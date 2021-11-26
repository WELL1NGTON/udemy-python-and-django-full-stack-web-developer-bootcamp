
#####################################
############### TODO ################
#####################################

# TODO: Finish it, the rules about "it is war" are too confusing for me to do at my own
# but for now the base logic is done, later i'll research this bad "game" to understand
# better how to implement that part of the game..


#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import math
from random import random, shuffle
from typing import List, Tuple

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Card:
    def __init__(self, suite: str, rank: str):
        self.__suite = suite.upper()
        self.__rank = rank.upper()

    def suite_symbol(rank: str) -> str:
        if rank == "H":
            return "♥"
        elif "D":
            return "♦"
        elif "S":
            return "♤"
        elif "C":
            return "♣"
        return "?"

    def suite(self) -> str:
        return self.__suite

    def rank(self) -> str:
        return self.__rank

    def value(self) -> int:
        return RANKS.index(self.__rank)

    def __str__(self) -> str:
        return self.__rank + Card.suite_symbol(self.__suite)

    def __eq__(self, __o: object) -> bool:
        if type(__o) is not Card:
            return False
        return self.__suite == __o.__suite and self.__rank == __o.__rank


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self, cards: list[Card] = [], generate_new: bool = False) -> None:
        if generate_new:
            self.__cards = []
            for s in SUITE:
                for r in RANKS:
                    self.__cards.append(Card(s, r))
            return

        self.__cards: list[Card] = cards

    def draw(self, ammount: int) -> list[Card]:
        ammount = ammount
        total = len(self)

        if total == 0:
            return []

        if total < ammount:
            ammount = total

        cards_drawn = self.__cards[total - ammount: total]
        cards_remaining = self.__cards[0:total - ammount]

        self.__cards = cards_remaining

        return cards_drawn

    def put_cards_bottom(self, cards: list[Card]) -> None:
        self.__cards = cards + self.__cards

    def cards(self) -> list[Card]:
        return self.__cards

    def shuffle(self) -> None:
        global shuffle
        shuffle(self.__cards)

    def split(self, halfs: int = 2) -> list['Deck']:
        ammount_cards = int(len(self)/halfs)
        decks: list['Deck'] = []

        for _ in range(halfs):
            decks.append(Deck(self.draw(ammount_cards)))

        for deck in decks:
            if len(self) == 0:
                break
            deck.put_cards_bottom(self.draw(1))

        return decks

    def __len__(self) -> int:
        return len(self.__cards)

    def __str__(self) -> str:
        return str(len(self)) + "x🂠"


class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards: list[Card]) -> None:
        super().__init__(cards=cards, generate_new=False)

    def take_top_card(self) -> Card:
        return self.draw(1)[0]

    def take_three_face_down_cards(self) -> list[Card]:
        return self.draw(3)

    def one_face_down_card(self) -> list[Card]:
        return self.draw(3)

    def __len__(self) -> int:
        return super().__len__()

    def __str__(self) -> str:
        return super().__str__()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name: str, hand: Hand) -> None:
        self.__name = name
        self.__hand = hand

    def print_cards(self) -> None:
        print(str(len(self)) + "x🂠")

    def play_card(self) -> Card:
        if not self.has_cards():
            return None
        drawn = self.__hand.draw(1)
        card = drawn[0]
        print(self, "played the card", card)
        return card

    def has_cards(self) -> bool:
        if len(self.__hand) > 0:
            return True
        return False

    def __str__(self) -> str:
        return self.__name


######################
#### GAME PLAY #######
######################

def turn(player1: Player, player2: Player) -> None:
    card_p = player.play_card()
    card_c = computer.play_card()
    if card_c.value() == card_p.value():
        it_is_war(player, computer)


def it_is_war(player1: Player, player2: Player) -> Player:
    print("It is war!")


def has_winner(player1: Player, player2: Player) -> bool:
    if not player1.has_cards() or not player2.has_cards():
        return True
    return False


print("Welcome to War, let's begin...")

starting_deck = Deck(generate_new=True)

starting_deck.shuffle()

splitted_deck = starting_deck.split(2)

player = Player("player", Hand(splitted_deck[0].cards()))

computer = Player("computer", Hand(splitted_deck[1].cards()))

while not has_winner(player, computer):
    turn(player, computer)

winner = None
if not player.has_cards():
    winner = computer
else:
    winner = player

print(winner, "has won the game!")
# Use the 3 classes along with some logic to play a game of war!
