#!/usr/bin/env python

matrix = [[1,2,3], [4,5,6], [7,8,9]] # Here we have 3 items in 1 list matrix, this is 2d list i.e. list inside list

# If there is a list inside list and both those lists inside 1 more list, then its called 3d list

# suppose we want to print 2nd list from the list matrix:
print(matrix[1])
print("\n")

# suppose we want to print all the items of list matrix, means 1 2 3 4 5 6 7 8 9
for sublist in matrix:
    for i in sublist:
        print(i)
print("\n")

# suppose we want to print the item 5 use:
print(matrix[1][1]) # first [1] means the 1st item in matrix which is [4,5,6] & another [1] means first item in the list [4,5,6] which is 5
print(matrix[2][0])
print("\n")

# type() function: to get the data type of the varibale, e.g:
s = 'amitesh' # i have a string called s, suppose we want to see its type:
print(type(s)) # Output shows <class 'str'>, means its type is string
print("\n")

# suppose we want to know the tyoe of our list matrix:
print(type(matrix)) # Output is <class 'list'>, means its tye is list
