class Card:
    suits = ["H","C","D","S"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def __init__(self, suit, rank):
        try:
            self.suit = suits.index(suit)
            self.rank = ranks.index(ranks)
        except:
            raise Exception("invalid suit or value")

    def toString(self):
        print(suits[self.suit] + ranks[self.rank])
