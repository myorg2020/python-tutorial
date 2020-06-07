#!/usr/bin/env python

# tuples are data strcture, like list.
# It can store any data type value, like lists.
# There is 1 difference that tuples are immutable while lists are mutable.

# Means no append, no insert, no pop, no remove
# tuples are defined in branckets ()

example = ('one', 'two', 'three')

# tuples are used for the cases where we know data would be fixed...suppose for example days of week,
# so we can use tuples like below:

# day = ('mon', 'tue')

# But we can also say that as lists are mutable and we can store any kind of data type so why to use tuples

# Actually tuples are faster than lists. tuples performace is better than lists, so where we know data would not
# change we can use tuples.

# we can use below methods and functions with tuples:
# 1. count - to count how many times an element is present in a tuple
# 2. index - to know at what position a particular element is declared inside our tuple
# 3. len function
# 4. can also use slicing. e.g.:
print(example[:2]) # Output is ('one', 'two')
