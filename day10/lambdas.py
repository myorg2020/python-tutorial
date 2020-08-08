#!/usr/bin/env python

# Lambda expression is anonymous function...It doesn't have any name

# Let see a normal function:
def add(a,b):
    return a+b
print(add(2,3))
print("\n")

# Now lets define the same in lambda. Here we are storing lambda expression in a variable
add2 = lambda a,b : a+b
print(add2(10,10))

multiply = lambda a,b : a*b
print(multiply(10,10))
print("\n")

# But Actually we don't use lambda expressions in a variable. we use it with built-in functions - map, reduce, filter

# Now lets the example/proof of statement that Lambda expression doesn't have any name
# Here we are just printing the function not calling(print(add())) it.
print(add) # Output is <function add at 0x109401a70>, we can see the name of funcion is add
print(add2) # Output is <function <lambda> at 0x109401cb0>, we can see it's just showing <lambda> there is no name to it
print(multiply) # Output is <function <lambda> at 0x109401dd0>, we can see it's just showing <lambda> there is no name to it
