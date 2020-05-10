#!/usr/bin/env python

# Taking 2 inputs from user in same line, use split func like below

name, age = input("Enter your name and age: ").split()
print("My name is " + name + " and age is " + str(age))
# Enter your name and age: Amitesh 30 (Here while entering the inputs give spave between 2 values)

name, age = input("Enter your name and age: ").split(",")
print("My name is " + name + " and age is " + str(age))
# Enter your name and age: Amitesh,30 (Here while entering the inputs give comma between 2 values)
