#!/usr/bin/env python

number1, number2, number3 = input("Enter the number1, number2 and number3 separated by comma: ").split(",")
# print(number1)
# print(number2)
# print(number3)
addition = int(number1)+int(number2)+int(number3)
# print(addition)
avg = (addition//3)
print("The Average of 3 numbers is: {}".format(avg)) # Using string formatting python 3
print(f"The Average of 3 numbers is: {avg}") # Using string formatting python 3.6
