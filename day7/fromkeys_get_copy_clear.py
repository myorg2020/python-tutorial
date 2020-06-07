#!/usr/bin/env python

# fromkeys method:
# This method is used to create a dictionary if we want to keep the same value for all keys:
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# dict.fromkeys[(all key names which we want to keep), 'value of keys']
# Here the value of all the keys are unknown
print(d)
print("\n")

# we can also use tuple instaed list
d1 = dict.fromkeys(('name', 'age', 'height'), 'unknown')
print(d1)
print("\n")

# suppose if we write like this:
d2 = dict.fromkeys("abc", 'unknown') # a,b,c will become separate keys {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}
print(d2)
print("\n")

# suppose if we use raneg function here
d3 = dict.fromkeys(range(0,11), 'unknown') # A dictionary will be created with key names from 1 to 10 and all of the keys will have values as unknown
print(d3)
print("\n")

# Another exmaple
d4 = dict.fromkeys(['name', 'age'], ['unknown', 'unknown']) # name and age both will get the value as : ['unknown', 'unknown']
print(d4)
print("\n")

# get method() -> Most used (This is the better way to access the keys of dictionary)
dget = {'name' : 'Amitesh', 'age' : 30}
print(dget.get('name')) # Will Print Amitesh
print("\n")

print(dget.get('names')) # suppose if you enter the names which is not there is dictionary. it will print None, it won't print any error
print("\n")

# Can simply make use of this in a loop like as usual:
if dget.get('name'):
    print("Present")
else:
    print("not present")
print("\n")

# clear method, to clear the dictionary ,means to make it empty
dclear = {'name' : 'Amitesh', 'age' : 30}
dclear.clear() # It will clear the dictionary: {}
print(dclear)
print("\n")

# copy method: if you want to make the copy your dictionary
dc = {'name' : 'Amitesh', 'age' : 30}
dcopy = dc.copy()
print(dcopy)
print(type(dcopy))
print("\n")


