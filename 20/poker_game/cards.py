import suite

class Card:
    """扑克牌类"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        """返回扑克牌的字符串表示"""
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __lt__(self, other):
        """比较两张牌的大小"""
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value
"""
# Card tests
card1 = Card(suite.Suite.SPADE, 5)
card2 = Card(suite.Suite.HEART, 13)
print(card1)  # ♠5
print(card2)  # ♥K
"""