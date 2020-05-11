#!/usr/bin/env python

# Strings in python are immutable, means the characters used in the string cannot be changed.

string = "string"
# print(string[1]) #Prints "t"

# If we want to change the "t" with "T", it cannot be done.
# string[1] = T
# print(string)

# Using replace() method, we can replace "t" with "T" but cannot change it in original string:
new_string = string.replace("t","T")
print(new_string)
print(string) # Still prints the original string without "T", means original string cannot be changed.

# This feature in python is called immutable, but in ruby strings are mutable it means original string can be changed.
