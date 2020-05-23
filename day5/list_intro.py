#!/usr/bin/env python

# list is data structures.
# list is collection of items. we can store anything in list: int, float, string
# We can create list using square bracket

# Here storing many intergers in one list numbers
numbers = [1, 2, 3, 4]
print(numbers)

# Here storing many strings in one list words
words = ["word1", "word2", 'word3']
print(words)

# Here storing strings, int, float in one list mixed
mixed = [1, 2, 3, 4, "word1", "word2", 'word3', 2.3, None]
print(mixed)

# suppose if we want any particular position only to print for list mixed,

mixed = [1, 2, 3, 4, "word1", "word2", 'word3', 2.3, None]
print(mixed[2])
print(mixed[5])

# suppose if we want to chnage any particular position in list mixed,

mixed = [1, 2, 3, 4, "word1", "word2", 'word3', 2.3, None]
mixed[3] = 'three'
print(mixed)

# suppose if we use below

mixed = [1, 2, 3, 4, "word1", "word2", 'word3', 2.3, None]
mixed[1:] = 'three'
print(mixed)

# suppose if we use below

mixed = [1, 2, 3, 4, "word1", "word2", 'word3', 2.3, None]
mixed[1:] = ['three', 'four']
print(mixed)
