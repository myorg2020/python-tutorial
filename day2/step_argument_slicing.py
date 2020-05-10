#!/usr/bin/env python

# syntax - [start argument:stop argument:step]
print("python"[0:5:2])

# 0 = p, -6
# 1 = y, -5
# 2 = t, -4
# 3 = h, -3
# 4 = o, -2
# 5 = n, -1

# Let's break this - 0:5 means, it will print pytho

# p - 0
# y - 1
# t - 2
# h - 3
# o - 4

# 0:5:2 means - first is 0:5 means we have to go from "p to o" i.e. pytho
# Adding :2 means - in pytho , it takes 2 steps - starting from p "pto"

print("python"[::3]) # No start and stop, it takes 3 step starts from p, ph
print("python"[5::-1]) # starts from n and goes till end (p) with -1
