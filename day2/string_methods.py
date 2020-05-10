#!/usr/bin/env python

name = "AmItEsH rAnJaN"

# 1. len() function - # len() function gives the count of number of characters in our string, including space
length = len(name)
print(length)

# Same thing can als be written as:
print(len("AmItEsH rAnJaN"))

# 2. lower() method - # lower method converts all the characters into lower case and should use with dot(.) in variable
print(name.lower())

# Same thing can als be written as:
low = name.lower()
print(low)

# 3. upper() method - # upper method converts all the characters into upper case and should use with dot(.) in variable
print(name.upper())

# 4. title() method - # title method converts 1st letter of a word into upper case & remaining in lower case and should use with dot(.) in variable
print(name.title())

# 5. count() method - # count method gives the count of a character used in the string and should use with dot(.) in variable, like below
print(name.count("a"))
print(name.count("A"))
