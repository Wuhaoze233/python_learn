import random
import cards
import suite

class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [cards.Card(suite, face)
                      for suite in suite.Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)
        self.current = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """是否还有牌"""
        return self.current < len(self.cards)

"""
# Poker tests
poker = Poker()
print(poker.cards)  # 洗牌前的牌
poker.shuffle()
print(poker.cards)  # 洗牌后的牌

"""