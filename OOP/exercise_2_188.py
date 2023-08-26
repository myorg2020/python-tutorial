class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.huygens_brand_name = brand_name
        self.huygens_model_name = model_name
        self.huygens_price      = price
        self.huygens_full_name  = brand_name + ' ' + model_name

    def apply_discount(self, num):
        discounted_price = (self.huygens_price*num)/100
        final_price = self.huygens_price - discounted_price
        return final_price
    
l1 = Laptop('Dell', 'Inspiron', 50000)
l2 = Laptop('HP',   'Aux',      40000)

print(f"laptop1 price is: {l1.huygens_price}")
print(f"laptop1 full name is: {l1.huygens_full_name}")
print(f"laptop2 price is: {l2.huygens_price}")
print(f"laptop2 full name is: {l2.huygens_full_name}")

print(f"Final price of laptop1 after discount is: {l1.apply_discount(10)}")
print(f"Final price of laptop2 after discount is: {l2.apply_discount(10)}")