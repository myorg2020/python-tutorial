#!/usr/bin/env python

user_info = {
    'name' : 'Amitesh',
    'age' : 30,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],

}

# To check if key exists in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')
print("\n")

# To check if value exists in dictionary
if 'Amitesh' in user_info.values(): # should use values() while checking for value
    print('present')
else:
    print('not present')
print("\n")

if 30 in user_info.values(): # here 30 is in integer and output would be present, if we use '30' then it consider it as string and output would be not present
    print('present')
else:
    print('not present')
print("\n")

if ['coco', 'kimi no na wa'] in user_info.values(): # to check for the list
    print('present')
else:
    print('not present')
print("\n")

# Looping in dictionaries
for i in user_info: # It prints only keys of this dictionary
    print(i)
print("\n")

for i in user_info.values(): # To print the values of this dictionary
    print(i)
print("\n")

# values() method
user_info_values = user_info.values() # it prints values like this: dict_values(['Amitesh', 30, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']])
print(user_info_values)
print(type(user_info_values))
print("\n")

# keys() method
user_info_keys = user_info.keys() # it prints keys like this: dict_keys(['name', 'age', 'fav_movies', 'fav_tunes'])
print(user_info_keys)
print(type(user_info_keys))
print("\n")

# items() method
user_info_items = user_info.items() # it prints keys & values both like this: dict_items([('name', 'Amitesh'), ('age', 30), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ['awakening', 'fairy tale'])])
print(user_info_items)
print(type(user_info_items))
print("\n")

# where is this method items() is useful:
for i, j in user_info.items():
    print(f"{i} : {j}")
