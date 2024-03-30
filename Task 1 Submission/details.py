'''
Practical Task 2 --- `details.py`

Psuedocode:

Use the `input()` command four times, each to collect a different
piece of information from the user and store them in unique variables.

Then use a single print statement to combine all of the user's input
into one sentence.
'''

# Wait for the user to input their name and store it in `name`.
name = input("What is your name? ")

# Wait for the user to input their age and store it in `age`.
age = input("How old are you? ")

# Wait for the user to input their House number and store it in
# `house_no`.
house_no = input("What is your House number? ")

# Wait for the user to input their Street name and store it in
# `street_name`.
street_name = input("What is your Street name? ")

# Combine all of the stores strings into one sentence and print it.
print("This is " + name + ". He is " + age + " years old and lives at house number " + house_no + " on " + street_name + ".")


