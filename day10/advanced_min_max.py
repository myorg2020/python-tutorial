#!/usr/bin/env python

# This is the Normal Usage of max() & min() functions
numbers = [1,2,3,4,5]
print(max(numbers))
print(min(numbers))
print("\n")

# Now we will see the advanced Usage of max() & min() functions

# Suppose we have a list of below strings and we want to know that item having maximum length

names = ['amitesh', 'abc', 'z']
print(max(names, key = lambda i : len(i))) # we get output amitesh
print("\n")

# Using above way we can use max() function. syntax max(iterable, key = function)

# Suppose we have below list with dictionary. we want to know the max name of student w.r.t maximum score

students = [
	{'name':'amitesh', 'score':90, 'age': 24},
	{'name':'saanvi', 'score':70, 'age': 22},
	{'name':'manisha', 'score':60, 'age': 25}
]
print(max(students, key = lambda i : i.get('score'))) # Output we get student with max score {'name': 'amitesh', 'score': 90, 'age': 24}
print(max(students, key = lambda i : i.get('score'))['name']) # here Output is amitesh.suppose we want only name, just take ['name'] key from that dictionary

# Suppose we want to know the student name with according to age having max age
print(max(students, key = lambda i : i.get('age'))['name']) # Output is manisha


# Example: Suppose we have this kind of Data Structure, In dictionary these is dictionary
# And we want to get the name of student with Maximum score
students1 = {
	'ranjan' : {'score':90, 'age':24},
	'saanvi' : {'score':70, 'age':22},
	'manisha' : {'score':60, 'age':25}
}

print(max(students1, key = lambda item : students1[item]['score']))
