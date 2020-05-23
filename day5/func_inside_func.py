#!/usr/bin/env python

# Using function inside function. In last greatest_of_3_numbers.py we have created a function greatestof3 to compare 3 numbers.

# we can also use the function used in exercise1.py (to compare greater of 2 numbers)

# mean we can use that function greater_than inside a function

def greater_than(a,b):
    if a>b:
        return a
    return b

# number1 = int(input("Enter the 1st number: "))
# number2 = int(input("Enter the 2nd number: "))
# result = greater_than(number1, number2)
# print(f"greater between {number1} and {number2} is: {result}")

# function inside function
def greatest(a,b,c):
    bigger = greater_than(a,b)
    return greater_than(bigger, c)

print(greatest(100,1000,1))

# Same can also be written as, exp devs used like this, but this may be confusing. So, keep it like above.
# Use kiss in programming: keep it simple stupid

def greatest(a,b,c):
    return(greater_than(greater_than(a,b), c))
print(greatest(1100,1000,130))
