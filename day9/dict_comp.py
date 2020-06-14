# dictionary comprehension. It's same like List comprehension.
# Only difference if that it had key:value pair.

# we will create a dictionary which will have number as key and value as it's square.

# square = {1:1, 2:4, 3:9,...upto 10} 

square_dict = {i:i**2 for i in range(1,11)}
print(square_dict)
print("\n")

# we want to print output like this:
# 'square of 1 is' : 1
# 'square of 2 is' : 4

square_dict = {f'square if {i} is' : i**2 for i in range(1,11)}
print(square_dict)
print("\n")

# If we want to print separately in next line:
square_dict = {i:i**2 for i in range(1,11)}
for k, v in square_dict.items():
    print(f"{k} : {v}")
print("\n")

# To print the count of characters of a string:
name = 'Amitesh'
count_dict = {i:name.count(i) for i in name}
print(count_dict)
print("\n")
# Explanation: we want the count of A m i t and so on
# it means A, m, i, t, e, s, h are keys and their counts are values.
# So we took i as key and value would be the count of i

name1 = 'ranjan'
count_dict1 = {i:name1.count(i) for i in name1}
print(count_dict1) # output is {'r': 1, 'a': 2, 'n': 2, 'j': 1}
