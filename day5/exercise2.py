#!/usr/bin/env python

def is_palindrome(string):
    reverse = string[::-1] # This is the logic to reverse a string, seen in string chapter
    if string == reverse:
        return True
    else:
        return False

name = input("Enter the string to check if it\'s palindrome: ")
print(is_palindrome(name))
