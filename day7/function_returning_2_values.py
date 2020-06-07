#!/usr/bin/env python

# If we return 2 values in a function, actually it gives those 2 values in a tuple.
# It won't give 2 separate values.

def func2(int1, int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply

print(func2(2,3)) # Output is (5, 6) - we can its returning both the values inside a tuple
print("\n")

# But we can use the trick and store these values in a separate variables and print them

add, multiply = func2(2,3)
print(add)
print(multiply)
