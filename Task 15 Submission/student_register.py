'''
Task 15
IO Operations - Output 

Practical Task --- `student_register.py`

'''

import os

'''
Clears terminal on various OS.
'''
def clear_screen():
    os.system('cls||clear')


'''
Error caused by incorrect user input.
'''
def display_error():
    print("Error: Invalid input. Please try again.")


'''
Gets the number of students registering for the exam from user input.
Handles invalid input by displaying an error message and prompting
the user to enter a valid integer.
'''
def get_student_count():
    input_message = "How many students are registering for the exam? "
    student_count = None

    while student_count == None:
        student_count = input(input_message)
        try:
            student_count = int(student_count)
        except ValueError:
            student_count = None
            clear_screen()
            display_error()
    
    return student_count

'''
Gets the student ID from user input, ensuring it only contains
alphanumeric characters and no spaces. Displays an error message for
invalid input.
'''
def get_studentID():
    input_message = "Please enter the next student's ID number: "
    studentID = input(input_message)

    while studentID.isalnum() == False:
        clear_screen()
        display_error()
        print(
"""A student ID number can only contain alphanumeric characters and no 
spaces.""" 
        )
        studentID = input(input_message)

    return studentID

# Get the number of students from user input
student_count = get_student_count()

# Write student IDs to a file
with open("reg_form.txt", "w") as file:
    for i in range(student_count):
        clear_screen()
        studentID = get_studentID()
        file.write(f"{studentID}\t..........\n")
