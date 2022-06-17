# File Name: deck.py
# Author Name: Lindsey Kim
# Date: 10/16/2020
# Course: COSC 1
# Short Description: This is a deck class that creates an object for a deck of 52 cards
#
from card import *
from random import *

NUM_SUITS = 4
NUM_VALUES = 13
DECK_SIZE = 52


class Deck:
    def __init__(self):
        self.card_list = []  # an array to store the cards of a deck

    # adds all 52 cards (one of each combination of value and suit) of a standard deck to the deck array
    def add_standard_cards(self):
        for suit in range(1, NUM_SUITS + 1):
            for value in range(1, NUM_VALUES + 1):
                self.card_list.append(Card(value, suit))

    # randomly shuffles the deck
    def shuffle(self):
        current_index = 0
        while current_index < len(self.card_list):
            random_index = randint(0, DECK_SIZE-1)  # finds a random index to switch positions with

            # switches the card at the current index with the card at the random index
            temp = self.card_list[random_index]
            self.card_list[random_index] = self.card_list[current_index]
            self.card_list[current_index] = temp

            # moves to the next card
            current_index += 1

    # deals out hand_size number of cards from the deck
    def deal(self, hand_size):
        # creates a mini deck for the hand
        hand = Deck()

        # moves the last card to the hand until the hand reaches the desired size
        while len(hand.card_list) < hand_size:
            size = len(self.card_list)
            added_card = self.card_list.pop(size-1)
            hand.card_list.append(added_card)

        return hand
