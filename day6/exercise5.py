#!/usr/bin/env python

# input -> [1, 2, 5, 8, 9, 8], [1, 2, 7, 6, 3, 9] & output = [1, 2, 9] (means it should print a list with common elements)

def common_elements(listarg1, listarg2):
    numbers3 = []
    for i in range(0,len(listarg1)):
        for j in range(0,len(listarg2)):
            if listarg1 [i] == listarg2 [j]:
                var = listarg1 [i]
                numbers3.append(var)
    return numbers3

numbers1 = [1, 2, 5, 8, 9, 8]
numbers2 = [1, 2, 7, 6, 3, 9]
print(common_elements(numbers1, numbers2))
