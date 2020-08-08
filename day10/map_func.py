#!/usr/bin/env python


# we have a list of below numbers and we want to get a list as output which gives square of these numbers

numbers = [1, 2, 3, 4]

# This can also be done in a normal way by defining a func:

def find_square(num):
	output = []
	for i in num:
		output.append(i**2)
	return output

print(find_square(numbers))
print("\n")


# Same we will see how to do using map() function

def square(a):
	return a**2

squares = list(map(square,numbers)) # we don't have specify function square as square() within map, converting squares into list 
print(squares)
print("\n")

# using map() function we can also use lamba expression without defining square function

squares = list(map(lambda a:a**2,numbers))
print(squares)
print("\n")

# Same thing we can also do using LC

output_square = [i**2 for i in numbers]
print(output_square)
print("\n")

# we can also do this without using map() & LC. we have to just define a square function like in line #22

new_list = []
for i in numbers:
	new_list.append(square(i))

print(new_list)
print("\n")

# when to mostly use map() function. When we have to use some pre-defined function like len() etc.
# suppose we have a list of below and we want to get the lenght of each item and we know for length we have len() function

words = ['abc', 'abcd', 'abcde']
length = list(map(len, words))
print(length)
print("\n")

# Important point: On map() function we can run loop, i.e. it's iterable. But we can run a loop only once on map function
# Means here we are running 2 loops but we get output only once as 3,4,5
# Means we can run loop onlt once on map() function

words = ['abc', 'abcd', 'abcde']
length = map(len, words)
for i in length:
	print(i)
print("\n")

for j in length:
	print(j)
print("\n")

# Here we get output twice as we are running loop on a list as usual way

words = ['abc', 'abcd', 'abcde']
length = list(map(len, words))
for i in length:
	print(i)

for j in length:
	print(j)







