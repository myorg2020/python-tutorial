#!/usr/bin/env python

# Output should be reverse: [4, 3, 2, 1]
def reverse_list(listarg):
    reverse = []
    for i in range(len(listarg)):
        popped_item = listarg.pop()
        reverse.append(popped_item)
    return reverse

numbers = list(range(1,5)) # Generates a list from [1, 2, 3, 4]
print(reverse_list(numbers))
