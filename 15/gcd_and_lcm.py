'''
最大公约数和最小公倍数 gcd and lcm

Author: Haoze Wu
Version: 1.0
'''

def gcd(a: int, b: int) -> int:
    while b % a != 0:
        a, b = b % a, a
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)