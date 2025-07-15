'''
求组合数 Combinatorial number C(m, n)

Author: Haoze Wu
Version: 1.1
'''

from math import factorial as f

m = int(input('m = '))
n = int(input('n = '))
combinatorial_num = f(n) / (f(m) * f(n - m))
print(f'The combinatorial number C({m}, {n}) is {combinatorial_num:.0f}')