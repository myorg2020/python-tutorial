#!/usr/bin/env python

# Exercise is suppose we have a below list
# [1,2,3], [4,5,6], [7,8,9]
# Output should be average = (1+4+7)/3, (2+5+8)/3, (3,6,9)/3

# First we will do it for 2 lists using zip function
def average_finder(list1,list2):
	average = []
	for pair in zip(list1,list2): # pair value would be (1,4), (2,5), (3,6)
		average.append(sum(pair)/len(pair))
	return average

print(average_finder([1,2,3], [4,5,6]))
print("\n")

# Now we will make this anonymous function to pass for any number of list
def average_finder(*args):
	average = []
	for pair in zip(*args): # Imp here: As *args takes input in tuple: ([], []) and here using zip function we are unpacking those lists from tuple
		average.append(sum(pair)/len(pair))
	return average

print(average_finder([1,2,3], [4,5,6], [7,8,9])) # output is in floating point: [4.0, 5.0, 6.0]
print("\n")

# If we want output in integer just use '//' instead '/' in line #21


# Now we will do the same in just 2 lines using lambda and LC together
average_finder_1 = lambda *args:[sum(pair)//len(pair) for pair in zip(*args)]
print(average_finder_1([1,2,3], [4,5,6], [7,8,9]))

# Lets break Line #31
# 1. Meaning of lambda *args:[sum(pair)/len(pair) for pair in zip(*args)] (lambda syntax: lambda input:ouput)
# 2. here output is in Lc - [sum(pair)/len(pair) for pair in zip(*args)], first what we want is average of pairs from where in *args
