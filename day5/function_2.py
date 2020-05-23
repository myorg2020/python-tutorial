#!/usr/bin/env python

def add_three(a,b,c):
    return a+b+c

print(add_three(5,5,5))

# NO need to write return in function always, we can also use it like this:

def add_three_1(a,b,c):
    print(a+b+c)

add_three_1(5,5,5)

# But using return in function is recommended as per above example
