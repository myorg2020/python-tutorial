def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply = multiply*i
    return multiply

print(multiply_nums(3,2,4,5))

# Suppose in above function we 1 more parameter with *args i.e. num
# It means the argument 3 will be treated as normal integer in num and only 2,4,5 will be consodered in *args
# we will get the output 40 not 120

def multiply_nums1(num, *args):
    multiply1 = 1
    for i in args:
        multiply1 = multiply1*i
    return multiply1

print(multiply_nums1(3,2,4,5))

# Suppose if we don't pass anything in argument we get output as empty tuple i.e.()

def multiply_nums2(*args):
    multiply2 = 1
    print(args)
    for i in args:
        multiply2 = multiply2*i
    return multiply2

print(multiply_nums2()) # output is () and 1

# Suppose if we don't pass anything in argument but in parameter we pass num and *args
# will get error becoz if we pass num as parameter the we must pass a argument. Error would is clearly saying:
# TypeError: multiply_nums3() missing 1 required positional argument: 'num'

# def multiply_nums3(num, *args):
#     multiply3 = 1
#     print(args)
#     for i in args:
#         multiply3 = multiply3*i
#     return multiply3

# print(multiply_nums3()) # output is () and 1

# if we pass 2 parameters but argument is empty we still get empty tuple.
# Means if we pass num1, num2 as parameter we have to must pass argument
def multiply_nums4(num1, num2 , *args):
    multiply4 = 1
    print(args)
    for i in args:
        multiply4 = multiply4*i
    return multiply4

print(multiply_nums4(3,2)) # output is () and 1


# Here only 5,6 are part of args so will get output as 30
def multiply_nums5(num1, num2 , *args):
    multiply5 = 1
    print(args)
    for i in args:
        multiply5 = multiply5*i
    return multiply5

print(multiply_nums5(3,2,5,6)) # output is () and 1

# we can't define normal arg i.e. num after *args. This will be an error.
# becoz if first pass parameter as *args all the arguments which we will pass will be considered inside *args

# so if we want to use a normal parameter with *args, we must pass it first

def multiply_nums(*args, num): -> wrong
def multiply_nums(num, *args): -> correct
