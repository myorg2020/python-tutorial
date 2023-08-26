# 1.
# Suppose discount offer is over and there is no offer. so we just need to do like this:
# Laptop.discount_percent = 0 , see line number 19, so class variable we have changed as 0 
# so it will print the price without discount and will show original Price.

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

Laptop.discount_percent = 0
print(f"laptop1 price is: {l1.huygens_price}")
print(f"laptop1 full name is: {l1.huygens_full_name}")
print(f"laptop2 price is: {l2.huygens_price}")
print(f"laptop2 full name is: {l2.huygens_full_name}")

print(f"Final price of laptop1 after discount is: {l1.apply_discount()}")
print(f"Final price of laptop2 after discount is: {l2.apply_discount()}\n")

# 2.
# Suppose if we want to print the namespace of an object, means what the variables that object is having...
# use __dict__ functionality to do this.

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

Laptop.discount_percent = 0
print(f"laptop1 price is: {l1.huygens_price}")
print(f"laptop1 full name is: {l1.huygens_full_name}")
print(f"laptop2 price is: {l2.huygens_price}")
print(f"laptop2 full name is: {l2.huygens_full_name}")

print(f"Final price of laptop1 after discount is: {l1.apply_discount()}")
print(f"Final price of laptop2 after discount is: {l2.apply_discount()}")

print(l1.__dict__)
print(l2.__dict__)
print("\n")

# 3.
# Now we will see if different laptop is having diff discount, so how do we handle this using class variable.
# In Method we need to use "self.discount_percent" instead using as "Laptop.discount_percent".
# And in line 90, 91 pass it as object.var=value i.e. l1.discount_percent = 50

class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        self.huygens_brand_name = brand_name
        self.huygens_model_name = model_name
        self.huygens_price      = price
        self.huygens_full_name  = brand_name + ' ' + model_name

    def apply_discount(self):
        discounted_price = (self.huygens_price*self.discount_percent)/100 # here we need to use self.discount_percent
        final_price = self.huygens_price - discounted_price
        return final_price
    
l1 = Laptop('Dell', 'Inspiron', 50000)
l2 = Laptop('HP',   'Aux',      40000)

print(f"laptop1 price is: {l1.huygens_price}")
print(f"laptop1 full name is: {l1.huygens_full_name}")
print(f"laptop2 price is: {l2.huygens_price}")
print(f"laptop2 full name is: {l2.huygens_full_name}")

l1.discount_percent = 50
l2.discount_percent = 50
print(f"Final price of laptop1 after discount is: {l1.apply_discount()}")
print(f"Final price of laptop2 after discount is: {l2.apply_discount()}")