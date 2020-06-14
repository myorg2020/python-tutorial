# using if statement in list comprehension, In last 2 exmaples we have seen for loop in LC

# Suppose we have a list and we want to get even numbers list

# Normal method:
def even_list(numlist):
    even_num = []
    for i in numlist:
        if i%2 == 0:
            even_num.append(i)
    return even_num

numbers = list(range(1,11))
print(even_list(numbers))

# Using List Comprehension: we can do it in just 2 lines, will use both for & if in LC
even_num_list = [i for i in numbers if i%2 == 0]
print(even_num_list) # Same output will come

# Using List Comprehension: we can do even create numbers list also in LC, above we are at least using numbers list using line #13
even_num_list_1 = [i for i in range(1,11) if i%2 == 0] # Here we are using range also in LC to create a list
print(even_num_list_1) # Same output will come

# Let create to print odd numbers from a list of 1 to 10 using LC:
odd_num_list = [i for i in range(1,11) if i%2 != 0]
print(odd_num_list) 
