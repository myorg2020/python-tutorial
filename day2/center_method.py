#!/usr/bin/env python

name = "Amitesh"

# Suppose if we want to add * sign in left and right of our string, like: **Amitesh**
# Use center() method

# we want to print: **Amitesh**  =  2+7+2 = 11, so in method we enter 11.
# suppose we want to print: ****Amitesh**** = 4+7+4 = 15. so in method we enter 15.

print(name.center(11,"*")) # Using this way we can add *
print(name.center(15,"*"))

# Take input from user, And whatever the length is, add 2 ** infront and 2 ** in last, like: **name**
name = input("Enter the name: ")
length = len(name)
print(name.center(length+4,"*"))
