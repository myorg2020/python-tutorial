#!/usr/bin/env python

age = input("Enter your age: ")
age = int(age)
if age<=0:
    print("NOT APPLICABLE !!!")
elif age>=1 and age<=3:
    print("Ticket is FREE !!!")
elif age >=4 and age<=10:
    print("Ticket price is: 150")
elif age >=11 and age<=60:
    print("Ticket price is: 250")
else:
    print("Ticket price is: 200")
