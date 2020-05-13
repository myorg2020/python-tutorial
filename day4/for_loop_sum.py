#!/usr/bin/env python

# sum of 1 to 10
# 1+2+3+4+....

total = 0
for i in range(1,11):
    total += i
print(total)

# Now we will ask user to give input and will sum:

number = int(input("Enter the number: "))
total = 0
for i in range(1,number+1):
    total += i
print(total)
