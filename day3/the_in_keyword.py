#!/usr/bin/env python

# 'in' keyword is used to check if a particular character exists in a string or not.
name = "Amitesh"
if 'A' in name:
    print("A is present in the string")
else:
    print("A is not present in the string")

# Can also directly use the string itself

name = "Amitesh"
if 'Z' in "Amitesh":
    print("Z is present in the string")
else:
    print("Z is not present in the string")
