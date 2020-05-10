#!/usr/bin/env python

number_one = input("Enter the first number: ")
number_two = input("Enter the second number: ")
total = number_one + number_two
print("total is " + total)

# Above program gives output as 54, suppose if we enter first number & second number as 5 and 4 respectively
# Actually it concatenates becoz we are taking input in string with double quote. So, its considering it as string.

# So to make string input as number use the function: int() , like below
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
total = number_one + number_two
print("total is " + str(total)) # Here using str func to add string with number

# Means: str function converts number into string:
# 4 -> "4"

# And int function converts string into number:
# "4" -> 4

# And float function converts string into float:
# "4" -> 4.0

number1 = str(4) # str is converting 4 into "4"
number2 = float("44") # float is converting "44" into 44.0
number3 = int("33") # int is converting "33" into 33
print(number2 + number3) # float and int can be added but output format would be in float, here output is 77.0
