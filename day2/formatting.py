#!/usr/bin/env python

# This is usual synatx which we have seen and is very long
name, age = "Amitesh" , 30
print("# Using usual syntax:")
print("Hello " + name + " your age is " + str(age))
print("\n")

# This is easier syntax used in python 3, using this syntax no need to worry about str fun like above
# {} is called place holder
name, age = "Amitesh" , 30
print("# Using python 3 syntax:")
print("Hello {} your age is {}".format(name, age))
print("\n")

# This is even much easier syntax used in python 3.6, using this syntax no need to worry about str fun like above
name, age = "Amitesh" , 30
print("# Using python 3.6 syntax:")
print(f"Hello {name} your age is {age}")
print("\n")

# We can also do some calculation using python 3 & python 3.6 syntax, like below:
print("## We can also do some calculation using python 3 & python 3.6 syntax, like below:")
print("\n")
name, age = "Amitesh" , 30
print("# Using python 3 syntax:")
print("Hello {} your age is {}".format(name, age + 2))
print("\n")

# This is even much easier syntax used in python 3.6, using this syntax no need to worry about str fun like above
name, age = "Amitesh" , 30
print("# Using python 3.6 syntax:")
print(f"Hello {name} your age is {age + 2}")
