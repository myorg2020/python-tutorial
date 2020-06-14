# Exercise is that pass a list as input ['amitesh', 'ranjan']
# And output should be ['Amitesh', 'Ranjan'] # First letter of string should be Caps
# And 1 more output we should get using some function ['Hsetima', 'Najnar'] # It should reverse the string and first letter of should be Caps
 
def rev_func(lis, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [i[::-1].title() for i in lis]
    else:
        return [i.title() for i in lis]

names = ['amitesh', 'ranjan']
print(rev_func(names, reverse_str = True)) # output would be ['Hsetima', 'Najnar']
print(rev_func(names)) # Output would be ['Amitesh', 'Ranjan']
print("\n")


# Explanation:
# Using this: reverse_str = True makes our input string as reverse.
# Line #5, Passing a list and **kwargs becoz we don't know if user has used reverse_str = True
# Line #6, **kwargs stores Key:value pair as dictionary and to check if user has used key:value 'reverse_str = True' or not, we will use get method on dictionary to check if that key:value is there or not
# Line #7, If it's there means 'reverse_str = True' in dictionary then reverse the names in list and first letter as Caps
# Else just Print the names and first Letter as Caps.

# Line#7 is LC, just breaking in Normal function to understand better:
def normal_func(lis):
    output = []
    for i in lis:
        output.append(i[::-1].title()) # first value of i is amitesh, then i[::-1] reverses the string 'amitesh' , applying the function title() makes first letter of reversed string as caps
    return output

names = ['amitesh', 'ranjan']
print(normal_func(names)) # Output would be ['Hsetima', 'Najnar']

