# sets is a data type
# It's unordered collection of unique items. means:

s = {1,2,3,2} # It's created using {} braces and there is no key:value pair in sets
print(s) # Output is {1, 2, 3} as it's the collection of unique items
print('\n')

# Indexing can't be use here also like dictionary. we can't use s[0] as it's unordered collection

# why do we use sets: To get the unique items. suppose i have a long list with duplicate items:
# we can use set function for this:
lis = [1, 2, 33, 4, 8, 8, 2, 9, 33]
s2 = set(lis)
print(s2) # we get only unique items {1, 2, 33, 4, 8, 9} in set
print(type(s2)) # it's a set: <class 'set'>
print('\n')

# we can again make it as a list: This is very important
s3 = list(s2)
print(s3)
print(type(s3))
print('\n')

# Set methods:
# 1. To add a item in a set
s1 = {1, 2, 3}
s1.add(4)
print(s1)
print('\n')

# To reomve a item from set:
s1.remove(3)
print(s1)
print('\n')

# but if we remove which is not there in our set
# s1.remove(5) # we get KeyError: 5 as item 5 is not even there in our set
# print(s1)
# print('\n')

# discard method
s1.discard(2) # so when we use discard method, it works like remove and that removes that item
print(s1)
print('\n')

s1.discard(5) # but when using discard method for a item which is not there in our set, it won't give any 'KeyError: 5' like remove 
print(s1)
print('\n')
# using discard method don't give any 'KeyError: 5' like remove, it will just print the set whatever existing is there

# To clear the set
s1.clear() 
print(s1) # output would be set()
print('\n')

# copy method
s2 = {4, 5, 6}
s3 = s2.copy()
print(s3)

# we can store integer, float, string etc in set (like below) but we can't store dictionary, tuple and list
store = {1, 2.3, 4.0, 'amitesh'}
