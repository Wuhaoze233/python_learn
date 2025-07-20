from poker import Poker
from player import Player

poker = Poker()
poker.shuffle()
players = [Player('Alpha'), Player('Beta'), Player('Charlie'), Player('Delta')]

for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f"{player.name} 的手牌：{player.hand}")