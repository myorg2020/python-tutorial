#!/usr/bin/env python

numbers = [1, 2, 3, 4] # List, tuples, strings are iterables
squares = map(lambda a:a**2, numbers) # map() & filter() functions are iterator

# Let understand diff b/w iterables & iterator

# first need to understand for for loop works in a list, tuple or string
for i in numbers:
	print(i)
print("\n")

# what happens when we run for loop on numbers list:
# 1. It creates a function called "iter"
# 2. Then whatever this function returns it runs next funtion on this, Like below

itr = iter(numbers)
print(next(itr)) # It will print 1
print(next(itr)) # It will print 2
print(next(itr)) # It will print 3
print(next(itr)) # It will print 4
# print(next(itr)) # It gives error i.e StopIteration
print("\n")

# Now Let's see what happens when we run for loop on squares. It doesn't create any iter() function.
# It directory run next function and gives output

print(next(squares)) # It will print 1
print(next(squares)) # It will print 4
print(next(squares)) # It will print 9
print(next(squares)) # It will print 16