#!/usr/bin/env python

# what are doc strings
# how to write doc strings
# how to see doc strings
# what is help function

def add(a,b):
    ''' this function takes 2 numbers and returns their sum '''
    return(a+b)

# Its good habit to use doc string while defining a function so that its helpful for a user to undersand
# Suppose we want to print the doc string for a fucntions, use below synatx
print(add.__doc__) # funcname.underscoreunderscoredocunderscoreunderscore
print("\n")

# Even All the built in fucntions like len(), sort(), max(), any() etc...all have doc string
# To see the doc string of that function:

print(len.__doc__)
print(max.__doc__)
print(sum.__doc__)

# Suppose we know there is function in python called sum, & want to see it's usage, use help function like below
print(help(sum))
