# kwargs as a parameter means keyword argument
# **kwargs actually returns a dictionary
# *args takes input in tuple & **kwargs takes input in dict

def func(**kwargs):
    print(type(kwargs))
    print(kwargs)

func(first_name = "Amitesh", last_name = "Ranjan") # kwargs takes argument as key:value pair

# suppose if i add one more key:value pair, it will easily take. Means as many as key:value pair we want can add in argument

func(first_name = "Amitesh", middle_name = "Ranjan", last_name = "Kumar")

# Running a Loop with **kwargs: The way we run a loop in dictinary same way we to rn here also

def func1(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func1(first_name = "Amitesh", last_name = "Ranjan")

# **kwargs with normal parameter...Like in *args we have seen
# This will give error: TypeError: func1() missing 1 required positional argument: 'name'
# def func1(name, **kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")

# func1(first_name = "Amitesh", last_name = "Ranjan") 

# Now suppose we pass a argument name also, this will not give any error.
def func1(name, **kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func1("Saanvi", first_name = "Amitesh", last_name = "Ranjan")

# Unpacking dictinary in **kwargs
def func2(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
d = {"name" : "Amitesh", "age" : 30}
func2(**d) # If we just pass like this: func2(d), this will give error. we have pass like func2(**d)

