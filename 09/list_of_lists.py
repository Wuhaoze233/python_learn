'''
嵌套列表 List of lists

Author: Haoze Wu
Version: 1.0
'''

import random
list_of_lists = [[random.randrange(1, 100, 2) for _ in range(6)] for _ in range(5)]
print(list_of_lists)