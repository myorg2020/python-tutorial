
# d = {1:'odd', 2:'even'....}
# we will create dictionary like above if number is odd we will write odd
# if number is even we will write even

odd_even = {i :('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)
