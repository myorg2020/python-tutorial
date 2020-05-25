#!/usr/bin/env python

# should return this - # [1, 2, 3, 4, 5, 6, 7] -> [[1, 3, 5, 7], [2, 4, 6]]

def odd_even(listarg):
    even = []
    odd = []
    for i in listarg:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    final = [odd, even]
    return final

numbers = [1, 2, 3, 4, 5, 6, 7]
print(odd_even(numbers))
