'''
字母计数器 Letter counter

Author: Haoze Wu
Version: 1.0
'''

sentence = input(f"Please input a sentence\n")
counter = {}
for letter in sentence:
    if letter.isalpha():
        counter[letter] = counter.get(letter, 0) + 1
sorted_keys = sorted(counter, key=counter.get, reverse=True)
for key in sorted_keys:
    print(f'{key}: {counter[key]}')