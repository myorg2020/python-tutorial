#!/usr/bin/env python

# Escape Sequence as Normal Text - we want exact ouput like: line A \n line B
# so use \\, which is considered as \
print("line A \\n line B")
print("line B \\t line C")
print("this is 4 backslash \\\\\\\\")

# suppose want output - \"\'
# (\') gives output as (')
# (\") gives output as (")
# (\\) gives output as \
print(" \\\" \\\' ")
