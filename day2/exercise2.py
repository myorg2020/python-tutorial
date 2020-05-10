#!/usr/bin/env python

name = input("Enter your name: ")
# A - 0, -7
# M - 1, -6
# I - 2, -5
# T - 3, -4
# E - 4, -3
# S - 5, -2
# H - 6, -1
# print(f"{name}"[-1::-1])
print(f"Reverse of your name is: {name[-1::-1]}") # Using python 3.6
print("Reverse of your name is: {}".format(name[-1::-1])) # Using python 3
