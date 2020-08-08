#!/usr/bin/env python

# example 1: Let's define a function to get if the number is even or odd

# Normal function 1:
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False

print(is_even(4))
print("\n")

# Normal function 2: Same can also be defined as
def is_even1(a):
    return a%2 == 0 # Either a%2 == 0 would be True or False

print(is_even(10))

# Now Let's use lambda Expression
is_even2 = lambda a : a%2==0 # How many input we are passing 1 so it's (lambda a) & what it will return (a%2==0 True/False)
print(is_even2(8))

# To get last letter of a string
last_char = lambda s : s[-1] # How many input we are passing, 1 string so it's (lambda s) & what it will return, last letter of a string(s[-1])
print(last_char('amitesh'))

# if else with lambda:

# Suppose we want to check if length of a string is greater than 5, we will normal function first:
def greater(string):
    if len(string) > 5:
        return True
    else:
        return False

print(greater('amitesh')) # Output True

# Let's See using Lambda now
greater1 = lambda string : True if len(string) > 5 else False
print(greater1('amit'))

# Same thing we can even reduce more, let see first normal one
def greater2(string):
    return len(string) > 5 # This condition would return Either True or False

print(greater2('amitesh'))

# Same using lamda
greater3 = lambda string : len(string) > 5
print(greater3('amit'))
