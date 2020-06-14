# how we will create a list inside list using LC

# example = [[1,2,3], [1,2,3], [1,2,3]] # we want this list to be craeted using LC

# Normal
new_list = []
for i in range(3):
    new_list.append([1,2,3])
print(new_list)

# Using LC
nest_list = [[i for i in range(1,4)] for j in range(3)]
print(nest_list) 

