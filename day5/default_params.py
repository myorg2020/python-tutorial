#!/usr/bin/env python

def user_info(first_name, last_name, age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info("amitesh", "ranjan", 30)
print("\n")

# If we write like this, it will overwrite 23 and takes 30
def user_info(first_name, last_name, age=23):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info("amitesh", "ranjan", 30)
print("\n")

# If we make age as default
def user_info(first_name, last_name, age = None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info("amitesh", "ranjan", 30)

# If we can't make 2nd item or 1st item as default and make last item as Parameter. This will give error.
# we should always make last Parameter in the function as default like above, age = None

# def user_info(first_name, last_name = "unknown", age):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your age is {age}")
#
# user_info("amitesh", "ranjan", 30)
