# we know that as soon as we create our object like below p1 and p2, it calls constructor i.e. INIT Method.
# In INIT Method we have defined to pass 3 variables, so when we create p1 object we do like this:
# p1 = Person('Amitesh', 'Ranjan', 17)
# But what if we want to create a new object p3 and want to pass like full string, like this suppose:
# p3 = Person('Amitesh,Ranjan,17') all in same line like a string. So we need to create our own constructor.
# To create class method we use decorator "@classmethod".
# we create our own method from_string(cls,string) and pass our cls keyword as it's syntax for creating class method
# and we also need to pass another argument as "string" becoz in our p3 object we want to pass like full line as string.
# like this: p3 = Person('Amitesh,Ranjan,17')
# so we need to break the string with comman and store in variables like:
# first,last,age = string.split(',')
# And then define our object, in instance method how we pass arguments , synatx is: class(argument as per init method)
# same way for class method, we will do class(argument as per class method), so cls(first,last,age)
# And return this.
# Now how we will create p3 object using class method, we can just do p3 = Person('Amitesh,Ranjan,17')
# we need to do p3 = Person.from_string('Amitesh,Ranjan,17'), see line #55

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.cassini_first_name    = first_name
        self.cassini_last_name     = last_name
        self.cassini_age           = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

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

p3 = Person.from_string('Amitesh,Ranjan,17')
print(p3.full_name())