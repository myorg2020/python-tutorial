#!/usr/bin/env python

fruits = ["grapes", "mangoes", "apple", "lemons", "king"]

# To delete a item from list, use pop() method
fruits.pop() # pop always deletes the last item from the list
print(fruits)

# suppose if we want to delete any specific item, suppose item at 3rd position
fruits.pop(3)
print(fruits)

# we can also use del operator to delete any item
del fruits[1]
print(fruits)

# suppose we don't know the item's position which we want to delete, but we know which item to delete
# use remove method
fruits.remove("grapes")
print(fruits)
