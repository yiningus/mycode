#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = ' '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your score?"))

# if input value was higher or equal to 25
if score >= 90:
    message = message + 'your score is A'
elif score >= 80:
    message = message + 'your score is B'
elif score >= 70:
    message = message + 'your score is C'
elif score >= 60:
    messae = message + 'your score is D'
else:
    message = message + 'sorry, your failed, and try again.'
print(message)

