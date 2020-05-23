#!/usr/bin/env python

# Using append methos we can append data in last position of our list
fruits = ["grapes", "apple"]
fruits.append("mango") # append method always appends data in the end of the list
print(fruits)

# If we want to append the data at any position in out list, use insert method:
fruits1 = ["grapes", "apple"]
fruits1.insert(1, "mango") # 1 means at 1st position, currently at 1st position its apple.
print(fruits1)

# To join 2 list means concatenating 2 lists;
fruits1 = ["grapes", "apple"]
fruits2 = ["oranges", "lemon"]
fruit = fruits1 + fruits2
print(fruit)

# extend method, suppose if we want to add 2nd list in 1st list, means extending 1st list
fruits1 = ["grapes", "apple"]
fruits2 = ["oranges", "lemon"]
fruits1.extend(fruits2)
print(fruits1)

# we can do the same using append as well, but if we use append fruits2 list itself will get appended
# Not like just contents of fruits2 into fruits1 using extend method
# output: ['grapes', 'apple', ['oranges', 'lemon']]
fruits1 = ["grapes", "apple"]
fruits2 = ["oranges", "lemon"]
fruits1.append(fruits2)
print(fruits1)
