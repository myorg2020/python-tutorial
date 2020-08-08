# we use enumerate function with for loop to track the position of our items in a list/tuple.
# Using normal for loop also we can track the position of our items in a list/tuple.

# Normal way:
name = ['abc', 'abcdef', 'amitesh']
# Suppose we want to get the items of our list using position, like below
# 0 : abc
# 1 : abcdef
pos = 0
for i in name:
    print(f"{pos} : {i}")
    pos += 1
print("\n")

# we get output with position
# 0 : abc
# 1 : abcdef
# 2 : amitesh

# Using enumerate function:
for pos, i in enumerate(name):
    print(f"{pos} : {i}")
print("\n")

# Define a function which take a argument: 1 list like above and one string.
# If the passed string is found in the list, return the position of that string in list
# else return -1
# We have to do this using enumerate function:

def find_position(lis, name):
    for pos, i in enumerate(lis):
        if i == name:
            return pos
    return -1

names = ['abc', 'abcdef', 'amitesh']
print(find_position(names, 'amitesh'))
