'''
统计 statistic

Author: Haoze Wu
Version: 1.0
'''

import statistics

from torch.fx.experimental.migrate_gradual_types.constraint_transformation import register_transformation_rule


def ptp(data):
    return max(data) - min(data)

def mean(data):
    return sum(data) / len(data)

def median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return mean(sorted_data[mid - 1:mid + 1])
    else:
        return sorted_data[mid]

def var(data, ddof=1):
    x_bar = mean(data)
    return sum((x - x_bar) ** 2 for x in data) / (len(data) - ddof)

def std(data, ddof=1):
    return var(data, ddof) ** 0.5

def cv(data, ddof=1):
    return std(data, ddof) / mean(data)

def describe(data):
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

def