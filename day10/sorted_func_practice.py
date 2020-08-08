#!/usr/bin/env python

# List:
fruits = ['grapes', 'mango', 'apple']
fruits.sort() #sort func prints the list in sorted form alphabetically
print(fruits) # output: ['apple', 'grapes', 'mango']
print("\n")

# Tuple:
fruits1 = ('grapes', 'mango', 'apple')
# There is no sort() method to be used with Tuples, with tuples we can used sorted() method
print(sorted(fruits1))
# output is ['apple', 'grapes', 'mango'], as tuples are immutable(original tuple fruits1 would be as it is), hence it gives output in a list in sorted order
print("\n")

# Set:
fruits2 = {'grapes', 'mango', 'apple'}
# with Set also sorted() method can be used. Set is also immutable.
print(sorted(fruits2))
# output: ['apple', 'grapes', 'mango']
print("\n")

# Now Lets take some advanced data Structure, we have a list & inside list there are dictionaries
# we will see how we can sort this as per price, means lowest price first and so on...
guitars = [
    {'model': 'yamaha f310', 'price': 84000},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 45000}
]

print(sorted(guitars, key = lambda dic:dic['price'])) # this will sort in the way, lowest price first & so on...
print("\n")
print(sorted(guitars, key = lambda dic:dic['price'], reverse=True)) # this will sort in the way, highest price first & so on...
