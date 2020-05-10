#!/usr/bin/env python

name, letter = input("Enter the name and the letter you wish: ").split()
# print(name)
# print(letter)
length = len(name)
print(f"The count of your name is: {length}")

# Here counting number of letter regardless of lower or upper case, explanation below
low = name.lower()
concat = low+letter
length1 = concat.count("a")
print(f"The count of letter a and A is: {length1}")

# Explanation below:
# ⇒  python3 exercise3.py
# Enter the name and the letter you wish: Amitesh a
# The count of your name is: 7
# The count of letter a and A is: 2
