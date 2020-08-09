#!/usr/bin/env python

# check 2 conditions at same time
# and , or

print("This is 'AND' statement example:")
print("'TRUE'  'AND' 'TRUE',  overall 'TRUE'")
print("'TRUE'  'AND' 'FALSE', overall 'FALSE'")
print("'FALSE' 'AND' 'TRUE',  overall 'FALSE'")
name = "amitesh"
age = 30
if name=="amitesh" and age==30:
    print("condition True")
else:
    print("condition False")
print("\n")
# and statement explanation:

# here we are checking 2 conditions at same time
# Remember, in case of "and" - suppose if LHS is false i.e. name=="mohit" then whole condition is false and else will print
# suppose if RHS is false i.e. age==20 then whole condition is false and else will print

# Means in case of and, if both the conditions are true then only it run print - print("Both name and age are correct")
# Even if a single condition is False then overall condition will be False


# or statement explanation:
print("This is 'OR' statement example:")
print("'TRUE'  'OR'  'TRUE',  overall 'TRUE'")
print("'TRUE'  'OR' 'FALSE', overall 'TRUE'")
print("'FALSE' 'OR' 'TRUE',  overall 'TRUE'")
name1 = "manisha"
age1 = 28
if name1=="manisha" or age1==29:
    print("condition True")
else:
    print("condition False")
# Even if a single condition is true then overall condition will be True
