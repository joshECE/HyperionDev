# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Error 1: Syntax (No parentheses).
# Original: 
# print "Welcome to the error program"
# Correction: 
print("Welcome to the error program")

# Error 2: Syntax (incorrect indentation from lines 11 - 30)

# Error 3: Syntax (No parentheses).
# Original: 
    # print "\n"
# Correction:
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# Error 4: Runtime (age_Str not initialized and the code tries to
# compare it with a string with == operator)
# Error 5: Runtime (age_Str is not purely numerical so can't be 
# converted to int)
# Original: 
    # age_Str == "24 years old" 
    # age = int(age_Str) 
# Correction: 
age_Str = "24 years old" 
age = int(age_Str[:2]) 

# Error 6: Runtime (age is int so can't concatenate with the strings
# around it)
# Original: 
    # print("I'm" + age + "years old.")
# Correction:
print(f"I'm {age_Str}")

# Variables declaring additional years and printing the total years of age
# Error 7: Runtime (cannot add years_from_now (str) to age (int))
# Original: 
    # years_from_now = "3"
    # total_years = age + years_from_now
# Error 11: Logical (the program should print the age from 3 years
# and 6 months from now, not just 3 years)
# Correction: 
years_from_now = "3.5"
total_years = age + float(years_from_now)

# Error 8: Syntax (no parentheses)
# Error 9: Logical ("answer_years" string should be total_years 
# variable)
# Original: 
# print "The total number of years:" + "answer_years"
# Correction:
print(f"The total number of years: {total_years}")


# Variable to calculate the total amount of months from the total amount of years and printing the result
# Error 10: Syntax (wrong variable name used (total instead of 
# total_years))
# Original: 
# total_months = total * 12
# Correction: (also converting to int from float to remove decimal)
total_months = int(total_years*12)

# Error 12: Syntax (No parentheses)
# Error 13: Runtime (total_months (int) can't concatenate with string)
# Original: 
# print "In 3 years and 6 months, I'll be " + total_months + " months old"
# Correction:
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer