#!/usr/bin/env python

# Write a function which will return last charatcetr of the name.
# Below program give that:
name = input("Enter name: ")
length1 = len(name) - 1
length2 = len(name) - 2
for i in range(length2,length1):
    last_pos = name[length1]
    print(f"last character of {name} is {last_pos}")
print("\n")

#But Using function, we can write like this:
def last_char(username):
    return username[-1]

last=last_char("amitesh ranjan")
print(f"last character of username is {last}")
print("\n")

# Function which will return if a number is odd or even
def odd_even(num):
    if num%2 == 0: # % modulo gives reminder
        return "even"
    else:
        return "odd"

print(odd_even(10))

# Same can also be written as:
def odd_even(num):
    if num%2 == 0: # % modulo gives reminder
        return "even"
    return "odd"

print(odd_even(11))

# Write a function which says if number is even retruns True otherwise False:
def is_even(num):
    if num%2 == 0: # % modulo gives reminder
        return True
    else:
        return False

print(is_even(10))

# Same can also be written as:
def is_even(num):
    if num%2 == 0: # % modulo gives reminder
        return True
    return False

print(is_even(7))

# It can be further reduces as, pythonic way:
def is_even(num):
    return num%2 == 0
print(is_even(17))

# Parameter and Argument:
# when defining a function, thing inside () is called Parameter, like in #56 "num" is Parameter
# when calling a function, thing inside () is called Argument, like in #58 "17" is Argument

# A function can also be defined without mentioning anything inside function Parameter, like:

def song():
    return "happy song"
print(song())
