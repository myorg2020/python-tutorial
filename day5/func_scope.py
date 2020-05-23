#!/usr/bin/env python

# def func():
#     x = 7 # local variable
#     return x
#
# def func2():
#     print(x)
#
# func2()

# In above example we cannot call x = 7 from func into func2. Becoz x = 7 is local variable and scope is only in func()

# Below is fine becoz x = 5 is global variable
x = 5 # Global variable
def func():
    x = 7 # local variable
    return x

def func2():
    print(x)

func2()
print(func())
print(x)
