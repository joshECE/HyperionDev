'''
Practical Task 1 --- `while.py`

'''

import os

#----------------------------------------------------------------------#
'''
Clears terminal on various OS.
'''
def clear_screen():
    os.system('cls||clear')

#----------------------------------------------------------------------#
'''
Only known error that can occur is caused by an incorrect user input.
'''
def display_error():
    print("Error: Invalid input. Please try again.")

#----------------------------------------------------------------------#
def display_info(average,valid_input):
    '''
    Displays the title and description of the program, along with 
    the current average.
    '''
    line = ("-------------------------------"\
            "-------------------------------")
    title = ("--------------------- Average Calculator "\
             "---------------------")
    description = (
'''
This program calculates the running average of the numbers you 
enter. When you enter "-1" the program will end.
''' 
    )
    
    clear_screen()
    print(line)
    print(title)
    print(description)
    print(f"Current average: {average}\n")


#----------------------------------------------------------------------#
def get_input_number():
    '''
    Converts a users input to a float. If the input cannot be
    converted to a float, an error message is displayed and the user
    is once again prompted to enter a number.
    '''

    while True:
        user_input = input("Please enter a number: ")
        try:
            return float(user_input)
        except ValueError:
            clear_screen()
            display_error()
            pass
    
#----------------------------------------------------------------------#
if __name__ == "__main__":
    total = 0 # sum of all input numbers
    count = 0 # number of input numbers
    average = 0

    input_number = 0

    # take a new user input, calculate the new average and display it
    # until. repeat until -1 is entered.
    while input_number != -1:
        display_info(average,input_number)

        input_number = get_input_number()

        count += 1
        total += input_number
        average = total/count


        




