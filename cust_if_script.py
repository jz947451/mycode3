#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = 'Please enter your score --'

# wrap connection in a int() to accept decimals as numbers
connection = int(input("prompts your numeric score?"))

# if input value was higher or equal to 25
if connection > 100:
    message = message + 'Beyond the score scope.'
elif connection >= 90:
    message = message + 'yyour score A'
elif connection >= 80:
    message = message + 'your score B'
elif connection >= 70:
    message = message + 'your score C'
elif connection >= 60:
    message = message + 'your score D'
elif connection < 60:
    message = message + 'your score F'
else:
    message = message + 'should be number.'
print(message)
