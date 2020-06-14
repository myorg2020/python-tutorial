# set comprehension is not much used
# In set there is value only.

# suppose we want to create a set which has square of numbers from 1 to 10

s = {i**2 for i in range(1,11)}
print(s)

# suppose we have list and we want to create a set from first letter of each names
names = ['amitesh', 'manisha', 'saanvi']
first = {i[0] for i in names}
print(first)