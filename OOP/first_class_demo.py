# we will see how to create a class, like this:
# class Person: - Always use your class name 1st letter as capital, it's not a rule, it's a convention.
# And end with colon, class Person:

# inside class we define a special kind of Method, i.e. INIT Method. This is also called constructor.
# def __init__(self, Attributes which our objects will have), we are defining here what would be the 
# attributes of upcoming objects in this class "Person".
# Always write "self" first and then Attributes of upcoming objects, e.g. what attributes a person can have,
# A person can have his first, last Name and age.

# Now we will create "instance variables" with the help of Atrributes.
# syntax is - self.var_name = attribute

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.individual_first_name = first_name
        self.individual_last_name  = last_name
        self.individual_age        = age
        self.individual_full_name  = first_name + ' ' + last_name # we can also create a instance var this way by coming other attributes

# Now create a object
p1 = Person('Amitesh', 'Ranjan', 36) # p1 is object/instance here, syntax is - object_name = class_name(Atrributes which an object can have which we have Already decided in class Person that what Atrributes a person can have)
p2 = Person('Abhinav', 'Ranjan', 33) # Another object p2 in class Person

# Whenever we create an object like above p1, p2 out INIT Method defined above gets called.

# self in INIT Method Represents out object i.e. p1, p2
# As soon as we created p1 object, it has called INIT Method. And self is p1 object and p1 is having it's first_name, last_name and age.
# so self is p1 it means INIT Method looks like:
# p1.individual_first_name = first_name             & first_name we have passed in object is 'Amitesh'
# p1.individual_last_name  = last_name              & last_name  we have passed in object is 'Ranjan'
# p1.individual_age        = age                    & age        we have passed in object is  36
# p1.individual_full_name  = first_name + last_name & it would be 'Amitesh Ranjan'

# Similarly, as we created p2 object, it has called INIT Method. And self is p2 object and p2 is having it's first_name, last_name and age.

print(p1.individual_first_name)
print(p2.individual_first_name)
# So output is - Amitesh

# we can also use f string to print
print(f"First Name is: {p1.individual_first_name}")
print(f"First Name is: {p2.individual_first_name}")

# In INIT Method by default argument which we pass is self and self is nothing but your object.
# self represents our object.
