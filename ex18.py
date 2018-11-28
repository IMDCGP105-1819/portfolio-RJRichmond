import random

#This is the base class which is defining the card properties such as the set it belongs to and the number.
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
