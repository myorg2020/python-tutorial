# class Circle:
#     def __init__(self, radius, pi):
#         self.oop_radius = radius
#         self.oop_pi     = pi

#     def circum(self):
#         return 2*self.oop_pi*self.oop_radius
    
# c1 = Circle(3, 3.14)
# print(c1.circum())

# c2 = Circle(2, 3.14)
# print(c2.circum())

# In Above example we see 2 things:
# 1. value of pi is same and common for all objects, so we need to pass it everytime with all objects
# 2. the value of pi is same hence in memory evertime this var will have a memory assigned, so wastage of memory

# So to come over this we can use class variable which will be common for all objects.
# see below how to declare a class variable and used in objects.
# Here we have declared a class variable as "pi = 3.14" and called in method as "Circle.pi"
# class variables are also called "class Attributes"

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.oop_radius = radius
        
    def circum(self):
        return 2*Circle.pi*self.oop_radius
    
c1 = Circle(3)
print(c1.circum())

c2 = Circle(2)
print(c2.circum())

print("\n")

# we will see another example of class variable. See exercise exercise_2_188.py in which we had passed
# a number as a discount.
# we will change here same code to use class variable.
# suppose discount percent is common, 10% for all laptops so we can declare a variable within class as
# discount_percent = 10 and then in method call it as "Laptop.discount_percent"

class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        self.huygens_brand_name = brand_name
        self.huygens_model_name = model_name
        self.huygens_price      = price
        self.huygens_full_name  = brand_name + ' ' + model_name

    def apply_discount(self):
        discounted_price = (self.huygens_price*Laptop.discount_percent)/100
        final_price = self.huygens_price - discounted_price
        return final_price
    
l1 = Laptop('Dell', 'Inspiron', 50000)
l2 = Laptop('HP',   'Aux',      40000)

print(f"laptop1 price is: {l1.huygens_price}")
print(f"laptop1 full name is: {l1.huygens_full_name}")
print(f"laptop2 price is: {l2.huygens_price}")
print(f"laptop2 full name is: {l2.huygens_full_name}")

print(f"Final price of laptop1 after discount is: {l1.apply_discount()}")
print(f"Final price of laptop2 after discount is: {l2.apply_discount()}")

# But there is 1 Problem here, it's very rare that there would same discount for every laptop.
# Suppose for laptop1 10% discount, laptop2 20% discount is there, so using a common class variable will not work here.
# we will see how to do this in next - see class_variable_2.py