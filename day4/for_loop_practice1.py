#!/usr/bin/env python

# 123 = 1+2+3

total = 0
number = input("Enter the number: ")
for i in range(0,len(number)):
    total += int(number[i])
print(total)
