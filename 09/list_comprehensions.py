'''
列表生成式 List comprehensions

Author: Haoze Wu
Version: 1.0
'''

list_comp = [2 * i for i in range(100) if i % 3 == 0 and i % 5 == 0]
#This will create a list containing the first 100 multiples of 2 that are also divisible by both 3 and 5.
print(list_comp)