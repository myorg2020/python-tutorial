#!/usr/bin/env python

# Output should be like below:
# ['abc', 'tuv', 'xyz'] -> ['cba', 'vut', 'zyx']

def reverse_item(listarg):
    r_item = []
    for i in listarg:
        reverse_of_i = i[::-1]
        r_item.append(reverse_of_i)
    return r_item

words = ['abc', 'tuv', 'xyz']
print(reverse_item(words))
