# More about get method ()

user = {'name' : 'Amitesh', 'age' : 30}
# print(user.get('name')) # This will give the value of key 'name' i.e. 'Amitesh'
print(user.get('names')) # This gives output as None becoz there is no such key in dictionary
print(user.get('names', 'not found !')) # Suppose we don't want to print None, can write our custom message to print after comma if that key is not found

# If we have samekey more than once in dictionary then later value would be printed.
# dictionary will not have same key as a twice
user = {'name' : 'Amitesh', 'age' : 30, 'age' : 31}
print(user)
