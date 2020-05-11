#!/usr/bin/env python

# This is very important
# In Python at many places we must have seen, just written as:

# if name:
    # print("anything")

# So what's this ?

# Explanation below:
name = "amitesh"
if name: # This is used to check if string is empty or not. True, if string is not empty
    print("string is not empty")
else:
    print("string is empty")

#  Suppose in below case if string is empty
name1 = ""
if name1: # This is used to check if string is empty or not. True, if string is not empty
    print("string is not empty")
else:
    print("string is empty")

# Where it is useful?, FOr the scenarios like below:

username = input("Enter your name: ")
if username:
    print(f"Your name is {username}")
else:
    print("you didn\'t enterted your name")
