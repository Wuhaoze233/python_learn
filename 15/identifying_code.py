'''
随机验证码生成 Random identifying code generation

Author: Haoze Wu
Version: 1.0
'''

import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def identifying_code_generation(*, code_len = 6):
    return ''.join(random.choices(ALL_CHARS, k = code_len))

if __name__ == '__main__':
    code_len = int(input('Please input the length of the identifying code: '))
    print(f'The identifying code is {identifying_code_generation(code_len = code_len)}')