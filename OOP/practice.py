class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.f_name = first_name
        self.l_name = last_name
        self.a_age  = age


p1 = Person('Amitesh', 'Ranjan', 38)
p2 = Person('Abhinav', 'Ranjan', 35)
p3 = Person('Abhinav', 'Ranjan', 35)
p4 = Person('Abhinav', 'Ranjan', 35)
p5 = Person('Abhinav', 'Ranjan', 35)

print(Person.count_instance)

# print(p1.f_name)
# print(p2.a_age)
