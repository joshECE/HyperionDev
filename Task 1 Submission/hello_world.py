'''
Practical Task 1 --- `hello_world.py`

Psuedocode:

Use an `input()` function to ask the user to input their name 
and assign it to a variable.
Include this variable inside of a `print()` function to output
their name in the terminal.

Repeat this for the user's age.

Use a separate print statement to print "Hello World!" on a new line.
'''

# Displays "What is your name?" on the terminal and waits for 
# the user to type in their name. When they do, their name 
# is saved to the variable `name` as a string.
name = input("What is your name? ")

# Displays "Your name is __" where __ is the text inputted by
# the user.
print("Your name is " + name)

# The next two lines repeat the same process but with the 
# user's age instead of name.
age = input("How old are you? ")
print("You are " + age + " years old.")

# Displays "Hello World!" in the terminal.
print("Hello World!")
