# File Name: card.py
# Author Name: Lindsey Kim
# Date: 10/16/2020
# Course: COSC 1
# Short Description: This is a card class that creates a card object
#

CLUBS = 1
SPADES = 2
DIAMONDS = 3
HEARTS = 4
JACK = 11
QUEEN = 12
KING = 13


class Card:
    def __init__(self, value, suit):
        self.suit = suit  # suit ie. clubs (1), spades (2), diamonds (3), hearts (4)
        self.value = value  # value of card ie. 1-10, jack, queen, or king

    # returns string in the form of "value of suit"
    def __str__(self):
        # translates number equivalent of suit to its name
        if self.suit == CLUBS:
            suit_name = "clubs"
        elif self.suit == SPADES:
            suit_name = "spades"
        elif self.suit == DIAMONDS:
            suit_name = "diamonds"
        elif self.suit == HEARTS:
            suit_name = "hearts"
        else:
            suit_name = "Invalid suit"

        # translates number equivalent of value to its name if it is jack, queen, or king
        # returns string in given format
        if self.value == JACK:
            return "Jack of " + suit_name
        elif self.value == QUEEN:
            return "Queen of " + suit_name
        elif self.value == KING:
            return "King of " + suit_name
        else:
            return str(self.value) + " of " + suit_name
