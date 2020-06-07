name = 'ranjan'
d = {'r' : 1, 'a' : 2, 'n' : 2, 'j' : 1, 'a' : 2, 'n' : 2}
print(d)
print("\n")

# Output would be: {'r': 1, 'a': 2, 'n': 2, 'j': 1}
# In dictionary if we mention 1 key twice, it will take that key only once.

# Like to acheive the same in list we used 'temp' var and checked if that letter is there then skip it.
# In dictionary no need to do that, dictionary it self will not take 2 keys, it will print just once like above.

# we will write a function for the same:
def word_counter(string):
    counter = {}
    for i in string:
        value = string.count(i)
        counter[i] = value
    return counter

print(word_counter('ranjan')) # Output is same as above
