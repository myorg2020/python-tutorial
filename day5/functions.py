#!/usr/bin/env python

def add_two(a,b):
    return a+b

total = add_two(4,5)
print(total)

# Can also be written as:

print(add_two(4,5))

# How to use function:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
total = add_two(a,b)
print(total)

# we can even also add 2 strings using same function:
first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
total = add_two(first_name, second_name)
print(total)
