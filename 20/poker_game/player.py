import poker

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_one(self, card):
        """摸牌"""
        self.hand.append(card)

    def arrange(self):
        """整理手牌"""
        self.hand.sort()