"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

while 1 > 0:

    user_input = raw_input("> ")

    tokens = user_input.split(" ")
    
    if tokens[0] == "q":
        break

    if tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))

    if tokens[0] == "-":
        print subtract(int(tokens[1]), int(tokens[2]))    

    if tokens[0] == "*":
        print multiply(int(tokens[1]), int(tokens[2]))

    if tokens[0] == "/":
        print divide(int(tokens[1]), int(tokens[2]))

    if tokens[0] == "square":
        print square(int(tokens[1]))

    if tokens[0] == "cube":
        print cube(int(tokens[1]))

    if tokens[0] == "pow":
        print power(int(tokens[1]), int(tokens[2]))

    if tokens[0] == "mod":
        print mod(int(tokens[1]), int(tokens[2]))


