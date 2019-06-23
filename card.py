class Card:
    suits = ["H","C","D","S"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def __init__(self, rank, suit):
        try:
            self.suit = self.suits.index(suit)
            self.rank = self.ranks.index(rank)
        except:
            raise Exception()

    def toString(self):
        return self.ranks[self.rank] + self.suits[self.suit]
