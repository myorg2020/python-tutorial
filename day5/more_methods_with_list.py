#!/usr/bin/env python

# count
# sort
# sorted Function
# clear
# copy

fruits = ["grapes", "mango", "apple", "banana", "kiwi", "apple", "king"]
print(fruits.count("apple")) # count method to count how may time apple appears in the list

fruits = ["grapes", "mango", "apple", "banana", "kiwi", "apple", "king"]
fruits.sort() # sort method to sort in alphabetic order
print(fruits)

numbers = [3, 5, 7, 1, 9]
numbers.sort() # sort method to sort in alphabetic order
print(numbers)

numbers = [3, 5, 7, 1, 9]
print(sorted(numbers)) # sorted function print the in alphabetic order while original list remains same
print(numbers) # This prints the numbers list as it is, sorted function only prints in sorted order while original list is in same order as it is

numbers = [3, 5, 7, 1, 9]
numbers.clear() # clear method to clear the list
print(numbers)

numbers = [3, 5, 7, 1, 9]
numbers_new = numbers.copy() # copy method to copy the contents of a list in a new list
print(numbers_new)
