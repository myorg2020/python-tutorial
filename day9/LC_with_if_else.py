# numbers = [1,2,3,4,5,6,7,8,9,10]

# output should be if item is odd print it's negative i.e. 1 then -1, 3 then -3
# if item is even multiply by 2 i.e 2 then 4, 4 then 8

# Normal way:
def output(lis):
    output_list = []
    for i in lis:
        if i%2 == 0:
            output_list.append(i*2)
        else :
            output_list.append(-i)
    return output_list

numbers = list(range(1,11))
print(output(numbers))

# Using LC:
output_lis = [i*2 if (i%2 == 0) else -i for i in numbers]
print(output_lis)
