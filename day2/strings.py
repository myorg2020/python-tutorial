#!/usr/bin/env python

# to add 2 strings(String Concatenation), use + sign.

first_name = "Amitesh" # To add some space between first name and last name, can also give some space after firts name like: first_name = "Amitesh "
last_name = "Ranjan"
baby_first_name = 'Saanvi'
baby_last_name = 'Shrivastava'

full_name = first_name + " " + last_name # To add space between first name and last name add some space like: " "
baby_full_name = baby_first_name + baby_last_name

print(full_name)
print(baby_full_name)

# print(full_name + 3) -> can't be done as cannot add string and a number

print(full_name + "3") # to Add a number with string use double quote, using " " makes a number as string

print(full_name + str(3)) # to Add a number with string, can als use a string func
# str function changes a number into string. means number 4 into string "4"

print(baby_full_name * 3) # To print multiple times, use * sign, it will print 3 times
