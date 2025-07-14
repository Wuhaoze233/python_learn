'''
解包 Pack and unpack

Author: Haoze Wu
Version: 1.0
'''

import timeit

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

print('%.4f secs' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=1000000))
print('%.4f secs' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=1000000))
