#!/usr/bin/env python

import random
winning_number = random.randint(1,100)
for i in range(1,101):
    guessing_number = int(input("Guess a number between 0 and 100: "))
    if guessing_number == winning_number:
        if i == 1:
            print(f"you win, and you guessed this number in 1st attempt")
            break
        print(f"you win, and you guessed this number in {i} times")
        break
    else:
        if guessing_number > winning_number:
            print("too high")
        if guessing_number < winning_number:
            print("too low")
