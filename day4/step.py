#!/usr/bin/env python

# for loop, range function have a hidden thing: step argument
# range(start argument:stop argument:step argument)

# Normal one:
for i in range(1,10):
    print(i)
print("\n")

# step argument: # to print odd numbers from 1 to 10
for i in range(1,10,2):
    print(i)
print("\n")

# step argument: # to print even numbers from 1 to 10
for i in range(0,10,2):
    print(i)
print("\n")

# step argument: # to print from 10 to 1
for i in range(10,0,-1):
    print(i)
