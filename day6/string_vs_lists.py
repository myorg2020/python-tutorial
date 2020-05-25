#!/usr/bin/env python

# Diff b/w strings and lists:

# String is immutable(can't change the string) but list is mutable

# suppose we have a string:

s = 'amitesh' # immutable means we can't change the same string s. suppose if i apply a method title, let see:
t = s.title()
print(t) # output is Amitesh, as title method will convert first letter into capital
print(s) # output is amitesh, we can see string s is same, no change in the original string s


# list is mutable:
l = ['word1', 'word2', 'word3']
l.pop()
print(l) # output is ['word1', 'word2'], we can see original list l itself is changed now. means list is mutable

# 1 more example. Can we add a character in string, no we don't have any method to do that
# but using append() method we can add a character in list

ll = ['word4', 'word5', 'word6']
ll.append('word7')
print(ll) # output is ['word4', 'word5', 'word6', 'word7'], here the word7 got added in the original list itself
