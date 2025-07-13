'''
掷色子6000次，统计每个点数出现的次数。

Author: Haoze wu
Version: 1.0
'''

import random

dice_counts = [0] * 6  # 初始化一个列表，记录每个点数出现的次数
for _ in range(6000):
    current_dice = random.randrange(1, 7)
    dice_counts[current_dice - 1] += 1
print('Dice counts:')
for dice_fig in range(1, 7):
    print(f'{dice_fig} appeared {dice_counts[dice_fig - 1]} times')