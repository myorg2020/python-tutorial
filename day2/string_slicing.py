#!/usr/bin/env python

lang = "python"

# 0 = p , -6
# 1 = y , -5
# 2 = t , -4
# 3 = h , -3
# 4 = o , -2
# 5 = n , -1

# Tp print more than 1 letter in a string we use this syntax
# syntax - [start argument : stop argument]
# Suppose to print: yt , start argument is 1 and stop argument should be (till t its 3 position means 0,1,2 so its 3,see position table up)
print(lang[1:3])

# To print ho
print(lang[3:5])

# To print hon
print(lang[3:6])

# NO stop argument,
print(lang[1:]) # NO stop argument here, so it goes till end

# NO stop argument,
print(lang[3:]) # NO stop argument here, so it goes till end

# NO start argument,
print(lang[:3]) # NO start argument here, so it starts from begining

# Its not like that i have define a variable, i can also do like this:
print("Amitesh"[2])
print("Amitesh"[3:7])
