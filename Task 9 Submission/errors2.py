# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Error 1: Runtime (Python thinks Lion is an undefined variable when
# it should be a string)
# Original:
# animal = Lion
# Correction: 
animal = "Lion"

animal_type = "cub"
number_of_teeth = 16

# Error 2: Logical (number_of_teeth and animal_type are ordered 
# incorrectly)
# Error 3: Logical (string is not formatted, when printed it will
# display the variables' placeholders instead of their values e.g. 
# {animal} instead of Lion) 
# Original: 
# full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
# Correction:
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# Error 4: Syntax (No parentheses)
# Original: 
# print full_spec
# Correction:
print(full_spec)