#!/usr/bin/env python

# we can use range func to create tuple like list:

tupes = tuple(range(1,10))
print(tupes) # we get a tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tupes)) # verify the type: <class 'tuple'>
print("\n")

# To convert a tuple into list
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9)) # Add list in prefix within ()
print(nums) # we get list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(nums)) # verify the type: <class 'list'>
print("\n")

# To convert a tuple into string
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9)) # Add str in prefix within ()
print(nums) # we get string: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(nums)) # verify the type: <class 'str'>
print("\n")

# To convert a list into string
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = str([1, 2, 3, 4, 5, 6, 7, 8, 9]) # Add str in prefix within ()
print(nums) # we get string: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(nums)) # verify the type: <class 'str'>
