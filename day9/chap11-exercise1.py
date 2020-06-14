# Create a function which takes input as a num and a list...suppose
# (3,[1,2,3]) output should be a list of like 3 power 1,2,3 like [1,8,27]

# If user didn't pass any *args then should print as You have not passed any args

def power_to(num, *args):
    if args:
        return [i**num for i in args] # This is using LC. [3,[1,2,3]] here i is 1,2,3 and num is 3
    else:
        return "You have not passed any args"

nums = [1,2,3]
print(power_to(3,*nums))
print("\n")

print(power_to(3,*[2,3])) # we can also pass a list like this
print("\n")

# print(power_to(3))

# Explanation of above code:
# Line #7 means, i.e. if args: (this means if args is empty)...e.g:

lis = [1,2,3]
if lis: # means if lis is empty then condition would be false
    print("List is not empty")
else:
    print("List is empty") 