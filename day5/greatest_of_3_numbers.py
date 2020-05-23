#!/usr/bin/env python

def greatestof3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c

number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
number3 = int(input("Enter the 3rd number: "))
result = greatestof3(number1, number2, number3)
print(f"greatest among {number1}, {number2} & {number3} are: {result}")
