#!/usr/bin/env python

# Suppose we have a below function which takes any number of input in integer or float this will give us sum

def sum_of_numbers(*args):
	total = 0
	for i in args:
		total += i
	return total

print(sum_of_numbers(1,2,3,4.0))
print("\n")

# But this function will have a problem if user gives input as string or a list like below
# print(sum_of_numbers(1,2,3,'amitesh',['amitesh'])) # we get error TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# So, using all function we can do in this way: Let's first check if the numbers given in input are integer or float then only add otherwise retrun some message
def sum_of_numbers(*args):
	# as we know *args takes input in tuple ()
	if all([(type(i) == int or type(i) == float) for i in args]): # here using all() in LC
		total = 0
		for j in args:
			total += j
		return total
	else:
		return "wrong input"

print(sum_of_numbers(1,2,3,'amitesh',['amitesh']))
print("\n")

# Let's Break Line #20
# First LC: we are checking if type of numbers passed are interger/float 
# our passed input is: 1,2,3,'amitesh',['amitesh'] , so firstly i value is 1
# Now it checks if 1 is int or float, it's int so [True] will come in List
# Now i is 2 and now list would be [True, True] and So on, list would be [True, True, True, False, False]
# When we apply all() on this: all([True, True, True, False, False]), this will give False, Means it will go to else statement