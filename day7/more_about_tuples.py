#!/usr/bin/env python

# 1. Looping in tuples:
mixed = (1, 2, 3, 4.0)
for i in mixed: # we can also use while loop with tuples
    print(i)
print("\n")

# 2. Declare Tuple with one element:
# num = (1) # This is int
# word = ('word1') # This is str
# print(type(num))
# print(type(word))
# print("\n")

# To declare one element inside tuple we should use comma
num1 = (1,) # This is <class 'tuple'>
word1 = ('word1',) # This is <class 'tuple'>
print(type(num1))
print(type(word1))
print("\n")

# 3. Tuple without parenthesis
mixed1 = 'one', 'two', 'three' # if we use like this it will conside it as tuple
print(type(mixed1))
print("\n")

# 4. Tuple unpacking: we will take here 3 variables and store elements of tuple inside variables
# we should exactly take the varibales, like here we have 3 elements in tuple so take 3 varibales
# if we take 2 variables, it will throw an error
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarists1, guitarists2, guitarists3 = (guitarists)
print(guitarists1)
print(guitarists2)
print(guitarists3)
print("\n")

# 5. List inside tuples: (this is a tuple in which there is a list inside it)
favorites = ('southern mangolia', ['tokyo ghoul times', 'landscape'])
# Actually with tuples we can't do pop(), append() or any method, but with the list inside this tuple we can use those methods:
favorites[1].pop() # favorites[1] means at 1st position list is there inside this tuple
print(favorites)
print("\n")

# 6. we can use min, max and sum methods with tuples:
mixed = (1, 2, 3, 4.0)
print(min(mixed))
print(max(mixed))
print(sum(mixed))
