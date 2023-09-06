# In this chapter we will see how to create and use class methods.
# we have Already seen how to create instance methods, e.g: def full_name(self)
# By default in instance methods it takes the object even if we don't write self within bracket.
# But as per convention we should write as "self".

# we use more instance methods not class methods, but we should know how to create and use class methods.

# Now we will see how to create a class method, we will see Now. we will do a program to print how many object/instance a class is having.
# same exercise which we did while learning instance methods, see "exercise_3_192.py".
# with same login we will create a class method.
# To create a class method we use decorator which is  @classmethod
# And in class method we pass keyword as cls, same way in instance methods we passed self
# And then we write variables cls.class variable, so here it's: cls.count_instance
# And see line 46 we call class method like this: Person.count_instances()

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.cassini_first_name    = first_name
        self.cassini_last_name     = last_name
        self.cassini_age           = age

    @classmethod # To use class method we use this decorator
    def count_instances(cls): # as per convention we should pass here keyword as cls
        total_count = cls.count_instance
        # return f"You have create {total_count} instances of Person class"
        return f"You have created {total_count} instances of {cls.__name__} class" # we can also print name of class as persion this way - {cls.__name__} 

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

print(Person.count_instances())