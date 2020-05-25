#!/usr/bin/env python

# create a function which takes argument as a list and returns in output as square of that list

def square_list(list):
    square = []
    for i in list:
        square.append(i**2)
    return square

numbers = list(range(1,5)) # Generates a list from [1, 2, 3, 4]
print(square_list(numbers))