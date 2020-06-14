# Parameters orders:
# PADK
# Parameter, *args, default parameter, **kwargs

# Befor starting Let's recall default parameter

def func(name = 'unknown', age = 24):
    print(name)
    print(age)

func() # Output would be unknown and 24. This is default parameter.

# Suppose we want to pass all 4 types of parametes in a function at same time.
# There is a certain order for passing these parameters:
# Parameter, *args, default parameter, **kwargs

# Example:
def params_order(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

params_order('Amitesh', 1,2,3, a = 1, b = 2) # name parameter has argument as 'Amitesh', *args here is 1,2,3 , last_name is default paramet & **kwargs are a = 1, b = 2

# we have to always pass paramets in same order...if passing all 4 together or any 2 of them together
# If we want to a parameter & default parameter, then order would be (name, last_name = 'unknown')
# If we want to a parameter & **kwargs, then order would be (name, **kwargs)
# Means we have to follow this order always - PADK

