# suppose we want to add 2 numbers:

def add(a,b):
    return a+b

print(add(2,3))
print("\n")

# But suppose we want to add 10 numbers then it will give error becoz we are passing only 2 argument in above function
# To overcome we use *args: means we can pass n number of arguments
# Here * will do this job, instead of args we can write anything but as per convention use args only

def all_total(*args):
    total = 0
    for i in args:
        total = total + i # OR, total += i
    return total

print(all_total(1,2,3,4)) # here we can enter any numbers, it will add all
