# Here we are creating Method inside class Person. Functions inside a class are known as Methods.
# For E.g.: Here we are creating a Method i.e. full_name() in class Person to Print Full Name a person.

class Person:
    def __init__(self, first_name, last_name, age):
        self.cassini_first_name    = first_name
        self.cassini_last_name     = last_name
        self.cassini_age           = age

    def full_name(self):
        fullname=str(self.cassini_first_name) + ' ' + str(self.cassini_last_name)
        return fullname
    
    def is_above_18(self):
        if self.cassini_age > 18:
            return "Age is greater than 18"
        else:
            return "Age is lesser than 18"
    
p1 = Person('Amitesh', 'Ranjan', 17)
p2 = Person('Abhishek', 'Ranjan', 19)
print(f"First Name of p1 object is: {p1.cassini_first_name}")
print(f"Full Name of p1 object is: {p1.full_name()}") # we have created an Instance method to print full name of a person
print(f"Full Name of p2 object is: {p2.full_name()}")

# Actually while applying a method full_name() on an object, it actually does below.
# First it takes the class Person and apply that method and pass the object like below.
# using below also it will give same Result but Right way to do is above way i.e. p2.full_name()
# print(Person.full_name(p2))

# Right way to do is above way i.e. p2.full_name() , same like as we do for pre-defined class like list.
# in list suppose if we have a object l=[1,2,3,4]
# so how we use method on l object, l.pop() or l.clear() in same way we should use for our own class and method also.
# So it should be p1.full_name() , syntax to apply method is object.method

print(f"Is p1 Age greater than 18: {p1.is_above_18()}")
print(f"Is p2 Age greater than 18: {p2.is_above_18()}")

# Same way we have created another method "is_above_18()" and checking Age of object if greater than 18

# These Methods are called instance Methods and we can perform functionality on instances