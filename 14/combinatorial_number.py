'''
求组合数 Combinatorial number C(m, n)

Author: Haoze Wu
Version: 1.0
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        return n * factorial(n - 1)

m = int(input('m = '))
n = int(input('n = '))
combinatorial_num = factorial(n) / (factorial(m) * factorial(n - m))
print(f'The combinatorial number C({m}, {n}) is {combinatorial_num:.0f}')