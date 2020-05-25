#!/usr/bin/env python

# split method: converts string into list
# we have also seen the usage of split method to take user input for multiple variables

user_info = "Amitesh 30" # This is a string
# Use split method to convert it into a list and break it from where space is there
user_info = "Amitesh 30".split()
print(user_info)
# output is in list now: ['Amitesh', '30']

# suppose if we have comman in our string so we can tell split to creak it from comma, e.g:
my_address = 'Bangalore,36'
my_address = 'Bangalore,36'.split(',')
print(my_address)
# Output is ['Bangalore', '36']

# join method: converts list into string
user_info = ['Amitesh', '30'] # This is a list, NOTE here: we have to keep 30 in string only i.e '30', suppose if we keep in integer like this: 30 there would be error. becoz we can join 2 string together not a string and a number
# Use join method to convert it into string. we have to tell join method to from where it needs to be converted into string
# becoz there are 2 items separated by comma. we will say join method to use from comma and join into string
print(','.join(user_info))
# Output is Amitesh,30

# we use split method more and join method little less
