#!/usr/bin/env python

# 1. Generate lists using range function, earlier we have seen range function with for loop:

numbers = list(range(1,11))
print(numbers) # we have output as list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n")

# 2. 1 more function of pop() method.

numbers = list(range(1,11)) # range function will generate a list call "numbers" here.
numbers.pop()
print(numbers) # we get [1, 2, 3, 4, 5, 6, 7, 8, 9], can see last item 10 is removed by pop()
print("\n")

# 1 hidden work here pop() is doing, it has removed 10 from above list, where is that item stored
# we can see like this, its used becoz there no loss of item and if we want to use later, can be used
popped_item = numbers.pop()
print(popped_item) # it return 10 which was removed
# To see this output 10 will have to comment lines 12 & 13 , otherwise it will again run the pop method(defined in line #17 on numbers list and removes 9 this time and shows us output 9 which is removed, so this is also fine)
print("\n")

# index method: it will give us the position of the item which is there in list
print(numbers.index(3)) # here we want to know the position of item 3 which is actually 2
print("\n")

# suppose i have another list numbers1
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers1.index(1)) # I want the position of 1, output is 0 becoz 1 is at 0th position
print("\n")

# here i added one more 1 in below list numbers2
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print(numbers2.index(1)) # I want the position of 1, output is 0 becoz by default it starts searching from 0th position and it has found 1 at 0th position
# But i want the position of 1 which is at 10th position
print(numbers2.index(1, 3)) # Output is 10. (1, 3): 1 means to search the item '1' and 3 means starts the searching from 3rd position

# here i added one more 1 in below list numbers3
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 7, 8, 1]
# suppose i want the position of 3rd '1' which is at 14th position
print(numbers3.index(1, 11)) # 1 means the item 1, 11 means that we know that upto 10th position already 1 is there so start searching from 11th position
print("\n")

# How to pass list in a function, we will create a function which converts values of a list into negative
# Create a list pass:

numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative_list(l): # passing argument in this function as list
    negative = [] # First declare an empty list and keep appending the negative value using a loop
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers4)) # output is [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
