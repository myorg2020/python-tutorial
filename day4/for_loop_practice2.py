#!/usr/bin/env python

name = input("Enter your name: ")
temp_var = ""
for i in range(0,len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
