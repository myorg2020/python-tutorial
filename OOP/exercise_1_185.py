class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.lap_brand_name = brand_name
        self.lap_model_name = model_name
        self.lap_price      = price
        self.lap_full_name  = brand_name + ' ' + model_name

l1 = Laptop('Dell', 'Inspiron', 50000)
l2 = Laptop('HP',   'AUX',      40000)

print(l1.lap_brand_name)
print(f"Laptop1 brand name: {l1.lap_brand_name}") # This way also can be used to print it, using f string
print(l2.lap_model_name)
print(f"Laptop2 model name: {l2.lap_model_name}") # This way also can be used to print it, using f string
print(l1.lap_full_name)
print(f"Laptop1 full name: {l1.lap_full_name}") # This way also can be used to print it, using f string
print(l2.lap_full_name)
print(f"Laptop2 full name: {l2.lap_full_name}") # This way also can be used to print it, using f string