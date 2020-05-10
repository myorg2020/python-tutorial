#!/usr/bin/env python

# replace () method
# find () method

string = "she is beautiful and she is good dancer"

# suppose if we want to remove spaces with underscore, use replcae method
# Syntax - replace(what we want to replace , with the item)
print(string.replace(" ","_"))

#OR

underscore = string.replace(" ","_")
print(underscore)

# Can also replace a word using replace() method
word = string.replace("is","was")
print(word)

# suppose if we want to replace first "is" with "was"
word1 = string.replace("is","was",1)
print(word1)

# find() method is used to find the position of a word in our string
findis = string.find("is") # it will find the position in the string where "is" starts
print(findis)

# Suppose in below example, i'm adding "is" in begining, it will show 0 position in output
string1 = "is she is beautiful and she is good dancer"

findis = string1.find("is")
print(findis)

# suppose if i want to search the word "is" not from the 0th position use below, it will show 7 position in output
findis = string1.find("is",1)
print(findis)

# suppose if in the variable string (line #6), we don't know the ist position of the word "is", so use below logic
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)
