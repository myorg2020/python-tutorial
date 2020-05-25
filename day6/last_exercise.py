#!/usr/bin/env python

# input -> [1, 2, 3, [1, 2], [3, 4]] -> output should come number of list being used inside this list i.e. 2

def list_count(listarg):
    l_count = 0
    for i in listarg:
        if type(i) == list:
            l_count = l_count + 1
    return l_count

numbers = [1, 2, 3, [1, 2], [3, 4]]
print(list_count(numbers))
