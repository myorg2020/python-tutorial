#!/usr/bin/env python

user_id = ['user1', 'user2', 'user3']
names = ['amitesh', 'saanvi', 'manisha']

# Suppose i want to combine userd id and names, means user1 as amitesh, user2 as saanvi and so on...
# we can use zip() function

print(zip(user_id, names)) # It just prints <zip object at 0x10afb3f50> as zip object
print("\n")
print(list(zip(user_id, names))) # Just printing output in proper way in list
print("\n")
print(dict(zip(user_id, names))) # this we can also convert into dictionary
print("\n")

# Suppose if you have a list which is having 2 items only and another list with 3 items.
# The zip function ends at with shorter list. Means where the shirter list end, zip() function will end

user_id1 = ['user1', 'user2']
names1 = ['amitesh', 'saanvi', 'manisha']
print(list(zip(user_id1, names1))) # Output would be: [('user1', 'amitesh'), ('user2', 'saanvi')]
print("\n")

# Suppose you have a list in which there are tuples with 2 ietms, like below:
# The this kind of list we can easily convert into dictionary
list_tuple = [('a', 1), ('b', 2)]
print(dict(list_tuple)) # we get a dictionary: {'a': 1, 'b': 2}
print("\n")

# Does zip() function only works with 2 lists. No, we can use it with many lists. E.g:
user_id2 = ['user1', 'user2', 'user3']
names2 = ['amitesh', 'saanvi', 'manisha']
last_names = ['ranjan', 'shrivastava', 'kumari']

print(list(zip(user_id2, names2, last_names)))
# print(dict(zip(user_id2, names2, last_names))) # This cannot be converted into dictionary as dict will have only 2 values key:value pair

# It means we can convert dictionary for below kind of lists which has tuple in list and only 2 values in that tuple, like below:
# list_tuple = [('a', 1), ('b', 2)]
