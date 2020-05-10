#!/usr/bin/env python

# strip method is used to remove spaces from anywhere in the string
# lstrip method is used to remove spaces from left in the string
# rstrip method is used to remove spaces from right in the string

name = "     Amitesh     "
dots = "................."
# when prints, this shows space both sides
value = name+dots
print(f"{value}")

leftspace = name.lstrip()
value = leftspace+dots
print(f"{value}")

rightspace = name.rstrip()
value = rightspace+dots
print(f"{value}")

space = name.strip()
value = space+dots
print(f"{value}")

# Suppose if there are space in between the value of a variable
# To remove spaces from everywhere use replace() method
baby = "     Saa   n  vi     "
dots = "..............."
removespace = baby.replace(" ","") # Using replace(" ",""), means remove spaces i.e. (" ") with no space i.e. ("")
value1 = removespace+dots
print(f"{value1}")
