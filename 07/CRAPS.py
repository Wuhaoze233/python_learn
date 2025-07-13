'''
CRAPS赌博游戏
'''

import random

money = 1000

while True:
    print(f'Current money: {money}')
    if money <= 0:
        print('You have no money left. Game over!')
        break
    bet = int(input(f'Enter your bet (0 to {money}): '))
    if bet > money:
        print(f'Maximum bet is {money}. Try again.')
        continue
    elif bet <= 0:
        print('Bet must be greater than 0. Try again.')
        continue
    else:
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            if current_point == 7 or current_point == 11:
                print(f'You rolled a {current_point}. You win!')
                money += bet
                break
            elif current_point == 2 or current_point == 3 or current_point == 12:
                print(f'You rolled a {current_point}. You lose!')
                money -= bet
                break
            else:
                print(f'You rolled a {current_point}. Try again!')
                continue

