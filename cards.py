import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}



class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} 0f {self.suit}"



class Deck():

    def __init__(self):
        self.cardList = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cardList.append(card)



    def __str__(self):
        testString = ''
        for i in self.cardList:
            testString = testString+ "\n" + str(i)

        return testString

    def shuffle(self):
        random.shuffle(self.cardList)

    def sendCard(self):
        self.shuffle()
        return self.cardList.pop(0)

    def __len__(self):
        return len(self.cardList)


class Hand():
    def __init__(self):
        self.cardInHand = []
        self.points = 0
        self.aces = 0

    def addCard(self, card):
        self.cardInHand.append(card)
        self.points += values[card.rank]
        if card.suit == 'Ace':
            self.aces+=1
            self.adjust_for_aces()
        self.adjust_for_aces()

    def __str__(self):
        testString = ''
        for i in self.cardInHand:
            testString += "  " +str(i)
        return testString

    def __len__(self):
        return self.points

    def adjust_for_aces(self):
        if self.points>21 and self.aces:
            self.points -=10
            self.aces -=1
