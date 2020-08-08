#!/usr/bin/env python

# Using zip() function we can combine 2 list like below
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

combined_list = (list(zip(list1, list2)))
print(combined_list) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print("\n")

# Now suppose we want to do opposite of it. Supose we have a list like below and we want to convert into 2 list list1 & list2 :
comb_list = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
list1, list2 = zip(*comb_list) # Using zip* we can unpack the lists from comb_list
print(list(list1))
print(list(list2))
print("\n")

# Suppose now we want to compare list1 & list2 and want to get maximum...means (1,6), (2,7)...
# whatever is maximum in that, just print maximum number. Lets use zip() func to do it
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

new_list = [] # Make an empty list
for i in zip(list1, list2): # When we apply zip on list1 & list2 it creates a pair like (1,6), (2,7), (3,8), (4,9), (5,10)
	new_list.append(max(i)) # first value of i would be (1,6) and max() takes maximum b/w 1 & 6 ....And so on
print(new_list)

