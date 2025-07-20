from enum import Enum

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


"""
# Suite tests
for suite in Suite:
    print(f'{suite} = {suite.value}')
"""