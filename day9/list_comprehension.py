# List comprehension is one of the most powerful way to create and work in a list.
# This is the pythonic way of working with lists

# Suppose we want to create a list which will give us the square of, from 1 to 10

# Using Normal way:
square = []
for i in range(1,11):
    square.append(i**2)
print(square)
print('\n')

# Using List comprehension:
square_list = [i**2 for i in range(1,11)]
print(square_list)
print('\n')
# Explanation: first we should think what ouput we want in our list. Here we want square of numbers. So first add i**2
# then range from 1 to 10 , so accordingly add for loop.


# Suppose we want to create list which gives us negative numbers from 1 to 10 

# Using Normal way:
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)
print('\n')

# Using List comprehension:
negative_list = [-i for i in range(1,11)]
print(negative_list)
print('\n')

# Same here also, first we need to think what we want in our list. we want negative numbers, so add -i
# then from where to where i.e. range,so add range function in for loop


# Suppose we want to create a list which gives us the 1st letter of each name from below list

# Using Normal way:
names = ['Amitesh', 'Saanvi', 'Manisha']
name = []
for i in names:
    name.append(i[0])
print(name)
print('\n')

# Using List comprehension:
name_list = [i[0] for i in names]
print(name_list)

# same way first add what we want in output, we want first letter of each name so that would be i[0] and then for loop from that variable where we have stored the names.

