#!/usr/bin/env python

# Dictionary is a kind of Data type
# why we use dictinaries ?
# Becoz to make use of real life data. Lists are not enough to represent real life data.

# For example we have below list 'user', having name, age, user's fav movies, user's fav tunes
# we can use to keep these data inside a list & a list inside list but this is not a good way to do this,
# so, we use dictinaries
user = ['Amitesh', 30, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]

# What are dictinaries
# it's an unordered collection of data in 'key : value' pair.

# To create dictionary in python we use curly braces, like below:
# name is key and value is Amitesh || age is key and value is 30
user = {'name' : 'Amitesh', 'age' : 30}
print(user) # This is dictionary - {'name': 'Amitesh', 'age': 30}
print(type(user)) # verify the type - <class 'dict'>
print("\n")

# There is one more way to create a dictionary
user1 = dict(name = 'Amitesh', age = 30)
print(user1)
print(type(user1))
print("\n")

# How to access data from your dictionary, there is no indexing method here like list becoz of unordered collection of data in 'key : value' pair
# we can't use like listname[position]
# we should use the name of 'key' itself inside [], like below:
user = {'name' : 'Amitesh', 'age' : 30}
print(user['name'])
print(user['age'])
print("\n")

# which type of data a dictionary can store?
# Anything: string, numbers, list, dictionary inside a dictionary, float etc.
# suppose we have below list:
user = ['Amitesh', 30, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]

# Let's see how to model it in a dictionary:
user_info = {
    'name' : 'Amitesh',
    'age' : 30,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],

}
print(user_info)
print(type(user_info))
print(user_info['fav_movies']) # suppose want to print fav_movies, use name of key inside []
print("\n")

# we can use dictionary easily to store complex data. we can store 2 user's value, will see later in details
# user_info_2 = {
#     user1 : {
#         'name' : 'Amitesh',
#         'age' : 30,
#         'fav_movies' : ['coco', 'kimi no na wa'],
#         'fav_tunes' : ['awakening', 'fairy tale'],
#
#     user2 :
# }

# How to add data in your empty dictionary:
userinfo = {} # This is an empty dictionary
userinfo['name'] = 'mohit' # enter the 'key : value' whatever you want to keep inside your dictionary
userinfo['age'] = 40
print(userinfo)
