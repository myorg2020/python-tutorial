#!/usr/bin/env python

numbers = [1,2,3,4,5,6,7,8,9,10]

# we have a list of numbers and we want to get even numbers output from this list, we defined a function like below 
def is_even(a):
	return a%2 == 0 

# return a%2 == 0 would be either true or false. Means if a%2 == 0 then it will return True

# Now we will see how to use this function in a filter function
# Syntax is filter(func name, iterable)

evens = tuple(filter(is_even, numbers)) # we are printing output in a tuple
print(evens)
print("\n")

# Same thing can be done using lambda

evens = tuple(filter(lambda a:a%2==0, numbers))
print(evens)
print("\n")


# Suppose we don't want to convert the output in tuple, i just want a simple output then just run for loop.
# As filter() func is iterable

evens = filter(lambda a:a%2==0, numbers)
for i in evens:
	print(i)
print("\n")

# Suppose is i run the loop twice for filter function, it will still give output only once as like map()
# map() & filter() functions are iterable only once.

evens = filter(lambda a:a%2==0, numbers)
for i in evens:
	print(i)

for j in evens:
	print(j)
print("\n")

# If we want to run a loop multiple times, just run it on a tuple or list as usual.

evens = tuple(filter(lambda a:a%2==0, numbers))
for i in evens:
	print(i)

for j in evens:
	print(j)
print("\n")

# Using LC:

even_list = [a for a in numbers if a%2==0]
print(even_list)