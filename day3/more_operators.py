#!/usr/bin/env python

name = "Amit"

# Suppose if we want to add esh, use below:
# name = name + "esh"
# print(name)

# But as per immutability, we cannot change the string. But above we are changing the value of variable i.e. name

# Same can also be done using:
name += "esh"
print(name)

age = 23
age1 = 24
# Suppose we want to add 2 & want to multiply 2, use:

age += 2
print(age)

age1 *= 2
print(age1)
