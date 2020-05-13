#!/usr/bin/env python

# Earlier we have seen using string with for like below:
name = input("Enter your name: ")
for i in range(len(name)):
    print(name[i])
print("\n")

# In python we can use like this as well:
name = "amitesh"
for i in name:
    print(i)
print("\n")

# In python we can even use like this as well:
name = "amitesh"
for i in "mohit":
    print(i)

# to add numbers: 1234 - 1+2+3+4

number = input("Enter a number: ")
total = 0
for i in number:
    total += int(i)
print(total)
