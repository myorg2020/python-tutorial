#!/usr/bin/env python

user_info = {
    'name' : 'Amitesh',
    'age' : 30,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],

}

more_info = {'State' : 'Bihar', 'hobbies' : ['tech', 'cricket', 'music']}

# suppose we want to add the dictionary more_info into the dictionary user_info
user_info.update(more_info)
print(user_info)
print("\n")

# Suppose if i have a key which is common in the dictionary, here i have name key common with user_info
# it won't add another name key. It will update the name key of more_info dictionary & will remove the name key of user_info
more_info = {'name' : 'Amitesh Ranjan', 'State' : 'Bihar', 'hobbies' : ['tech', 'cricket', 'music']}
user_info.update(more_info)
print(user_info)
print("\n")

# Suppose i keep the dictionary empty in update method, it will just print the dictionary user_info as it is.
user_info.update({})
print(user_info)
print("\n")

