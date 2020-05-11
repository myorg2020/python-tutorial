#!/usr/bin/env python

winning_number = 50
guessing_number = input("Guess the number in between 40 to 60: ")
guessing_number = int(guessing_number)
if guessing_number == winning_number:
    print("YOU WIN !!!!")
else:
    if guessing_number > winning_number:
        print("too high")
    else:
        print("too low")


# This is called Nested if-else
        # if guessing_number == winning_number:
        #     print("YOU WIN !!!!")
        # else:
        #     if guessing_number > winning_number:
        #         print("too high")
        #     else:
        #         print("too low")
