#!/usr/bin/env python

def greater_than(a,b):
    if a>b:
        return a
    return b

number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
result = greater_than(number1, number2)
print(f"greater between {number1} and {number2} is: {result}")
