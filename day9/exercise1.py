
# lis = ['abc', 'tuv', 'xyz'] -> ['cba', 'vut', 'zyx']

# Normal method:
words = ['abc', 'tuv', 'xyz']
opposite = []
for i in words:
    opposite.append(i[::-1])
print(opposite)
print('\n')


# Using List comprehension:
opposite_list = [i[::-1] for i in words]
print(opposite_list)
print('\n')

# Using above same login, can also write a function for this list comprehension
def reverse_string(arglist): 
    return [i[::-1] for i in arglist]

print(reverse_string(words))


