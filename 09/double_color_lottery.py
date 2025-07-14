'''
双色球彩票模拟 Double color lottery simulation

Author: Haoze Wu
Version: 1.0
'''

import random
from rich import inspect

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

lottery = random.sample(red_balls, 6)

for ball in lottery:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

blue_ball = random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

inspect(red_balls, methods=True)