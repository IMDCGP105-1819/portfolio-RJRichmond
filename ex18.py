import random

#This will be the base class it will have all of the defining features such as number and set it belongs to.
class Card(object):
    def __init__(self,number,set):
        self.set = set;
        self.number = number;
    def __str__(self):
        Cards = []
        if self.number == 1:
            Cards.append("Ace")
        elif self.number == 11:
            Cards.append("Jack")
        elif self.number == 12:
            Cards.append("Queen")
        elif self.number == 13:
            Cards.append("King")
        else:
            Cards.append(str(self.number))
# This is checking to see if a card has any numbers which would normally be a picture card and changes it to the name of the card.
        if self.set == 0:
            Cards.append("♠")
        elif self.set == 1:
            Cards.append("♥")
        elif self.set == 2:
            Cards.append("♦")
        elif self.set == 3:
            Cards.append("♣")
        Cards.append("|")
# This checks which suit the card belongs to and gives the symbol accordingly.
        return Cards

    def CardSet(self,set):
        self.set = set

    def CardNumber(self,number):
        self.number = number

"""
This class is going to be the deck so it will have a way to reset the deck which will be drawing cards,
a way to deal and a way to be able to shuffle the deck as well.
"""
class Deck(object):
    def __init__(self,cards):
        self.cards = cards;

    def __str__(self):
        Cards = []
        for card in self.cards:
            Cards.append(card.__str_())

    def Reset(self):
        self.cards = []
        for i in range(53):
            if i <= 12:
                self.cards.append(Card(i+1,0))
            if i > 13 and i <= 26:
                self.cards.append(Card(i-13,1))
            if i > 26 and i <= 39:
                self.cards.append(Card(i-26,2))
            if i > 39:
                self.cards.append(Card(i-39,3))
# The reset function is the reseting the deck by putting all cards back into it.
