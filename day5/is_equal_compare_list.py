#!/usr/bin/env python

fruits1 = ["grapes", "mango", "apple"]
fruits2 = ["banana", "kiwi", "apple", "king"]
fruits3 = ["grapes", "mango", "apple"]

# To compare 2 lists use ==
print(fruits1 == fruits3) # Output is True, == compares the values of 2 lists
print(fruits1 == fruits2) # Output is False becoz values are different

# is keyword
print(fruits1 is fruits3) # Output is False becoz 'is' compares the memory location
print(fruits1 is fruits2) # Output is False becoz 'is' compares the memory location
print(fruits2 is fruits3) # Output is False becoz 'is' compares the memory location

# here 'is' is comparing if  fruits1, fruits2 and fruits3 are at same meory location.
# All 3 are different objects and are stored at different memory location, so output is False
