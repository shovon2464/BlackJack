import cards

class Player():

    def __init__(self):
        self.hand = cards.Hand()
        self.bank = 20

    def __str__(self):
        return f"Cards are {str(self.hand)} and point is -  {self.hand.points}"

    def show_first_deal(self):
        return f"Cards are {str(self.hand)} and point is -  {self.hand.points}"

    def show_first_deal_private(self):
        return f"Cards are  {str(self.hand.cardInHand[0])}"

    def hit_for_human(self,card):
        self.hand.addCard(card)


