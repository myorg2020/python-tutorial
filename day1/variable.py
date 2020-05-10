#!/usr/bin/env python

number1 = 2
print(number1)
# we can always change the value of variable like below
number1 = 4
print(number1)

# can also store string in a variable
name = "amitesh"
print(name)

# can also store the integer in same variable in which we have stored a string
name = 108
print(name)

# That's why python is called dynamic programming language, in which data type gets changed in variable

# variable naming rules:
# 1. variable cannot start with a number like below:
# 1number = 4
# print(1number)

# but a number can be used in between a variable
numb1er = 65
print(numb1er)

# 2. you can start your variable with any letter or with underscore (_)
name = "amitesh"
print(name)

_ = "amitesh"
print(_)

# 3. variable cannot start with any special character...special character can't even used in between of any variable.
# $usd = 34
# print("$usd")
#
# us%d = 68
# print("us%d")


### Naming conventions of variables:
user_one_name = "snake case" # snake case writing, it's recommended in python
print(user_one_name)
# means if using more than 1 word in a variable split it using underscore

userOneName = "camel case" # camel case writing, mostly used in Java
print(userOneName)

# But not much difference in between and can be used accordingly anytime.
