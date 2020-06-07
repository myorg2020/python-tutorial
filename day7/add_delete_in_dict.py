#!/usr/bin/env python

user_info = {
    'name' : 'Amitesh',
    'age' : 30,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],

}

# To add data in dictionary:
user_info['fav_songs'] = ['song1', 'song2']
print(user_info)
print("\n")

# To delete a key : value pair from dictionary: we must pass a argument in pop() in dictionary
popped_item = user_info.pop('fav_tunes') # suppose we want to delete 'fav_tunes' key and value from dict
print(f"popped item is {popped_item}") # see the value what it deletes
print(type(popped_item))
print(user_info) # see the original dict if it has deleted the 'fav_tunes' key and value
print("\n")

# popitem() method: is used whenever we want to delete any random key value pair
pop_item = user_info.popitem() # no need to enter any argument, it delets any random key value pair
print(user_info)
print(pop_item)
print(type(pop_item))
