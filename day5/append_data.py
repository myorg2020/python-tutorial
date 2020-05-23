#!/usr/bin/env python

# using append method we can append data to our list
# suppose we want to add 1 more item called mango in our list fruits, use:
fruits = ["grapes", "apple"]
fruits.append("mango") # append method always appends data in the end of the list
print(fruits)

# But in realtime we don't know how many data we are going to add/store/append in our list.
# so, we take a empty list like below and keep appending data into it:

real_list = []
real_list.append("data1")
real_list.append("value")
real_list.append("five")
print(real_list)
