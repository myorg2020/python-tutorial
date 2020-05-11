#!/usr/bin/env python

name, age = input("Enter name and age separated by space: ").split()
age = int(age)
name_first_char = name[0]
if name_first_char=="a" and age>10:
    print("you can watch coco movie")
else:
    if name_first_char=="A" and age>10:
        print("you can watch coco movie")
    else:
        print("sorry, you cannot watch coco")
