s = {'a', 'b', 'c'}

# in keyword:
if 'a' in s:
    print('present')
else:
    print('not present')
print('\n')

# for loop:
for i in s:
    print(i) # a, b, c can get printed in any order as it's unordered collection like dictionary
print('\n')

# union and intersection method for set: Most important -
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

union_set = s1 | s2 # union symbol is pipe (|)
print(union_set) # output is {1, 2, 3, 4, 5, 6}
print('\n')

# Explanation of union:, if we do union it gets joined: {1, 2, 3, 4, 3, 4, 5, 6}
# but in set we can't have duplicate items so it will print: {1, 2, 3, 4, 5, 6}

# Intersection means comman
intersection_set = s1 & s2 # intersection symbol is and (&)
print(intersection_set) # output is {3, 4} as it's common in s1 & s2
