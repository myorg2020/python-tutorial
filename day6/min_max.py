#!/usr/bin/env python

# min & max function is used to find lowest and greatest number in a list respectively.

numbers = [6, 60, 2]

print(min(numbers))
print(max(numbers))
print("\n")


# Function to get the diff b/w greatest & minimum
def diff(listarg):
    ma = max(numbers)
    mi = min(numbers)
    val = ma - mi
    return val

print(diff(numbers))
