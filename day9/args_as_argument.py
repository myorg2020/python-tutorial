def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply = multiply*i
    return multiply

print(multiply_nums(3,4,5))
print("\n")

# Below Example: 
def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply = multiply*i
    return multiply

num = [2,3,4] # suppose if we have a list as num and we pass num in the function, the function multiply_nums won't work. we will get list num as output.
print(multiply_nums(num))
print("\n")

# So, to pass a list as *args , we should pass *num as argument
def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply = multiply*i
    return multiply

num = [2,3,4] 
print(multiply_nums(*num))
print("\n")
