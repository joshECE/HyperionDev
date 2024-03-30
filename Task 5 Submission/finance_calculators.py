"""
Capstone Project --- `finance_calculators.py`

"""

import math
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
    clear_screen()
    print("Error: Invalid input. Please try again.\n\n")

#----------------------------------------------------------------------#

def input_and_check_float(display_str):
    '''
    Repeatedly requests an input until the input string can be 
    converted to a float. Display an error each time the string is
    invalid.
    '''
    while True:
        try:
            user_input = float(input(display_str))
            return user_input
        except ValueError:
            display_error()
        except:
            print("unknown error")


#----------------------------------------------------------------------#
def user_inputs(input_stage):
    '''
    Print a specific message to the console and/or request specific user
    input depending on the current stage of the program. Returns the
    relevant values.
    '''
    clear_screen()
    if input_stage == "program select":
        while True:
            print("investment - to calculate the amount of interest "\
                "you'll earn on your investment")
            print("bond       - to calculate the amount you'll have "\
                "to pay on a home loan")
            program = (
                input("\nEnter either 'investment' or 'bond' from the "\
                    "menu above to proceed: "))
            program = program.lower()
            if program == "investment" or program == "bond":
                return program
            else:
                display_error()
    
    elif input_stage == "select investment type":
        while True:
            print("Please select the type of investment.")
            interest = input('Type "simple" or "compound": ').lower()
            if interest == "simple" or interest == "compound":
                return interest
            else:
                display_error()

    elif input_stage == "investment values":   
        deposit = input_and_check_float(
            "Please enter the amount of money you will deposit (£): ")
        inv_rate = input_and_check_float(
            "Please enter the interest rate of your investment (%): ")
        years = input_and_check_float(
            "Please enter the length of your investment (years): ")
        return deposit, inv_rate, years
    
    elif input_stage == "bond values":
        house_value = input_and_check_float(
            "Please input the current value of the house (£): ")
        bond_rate = input_and_check_float(
            "Please enter the interest rate on the bond (%): ")
        months = input_and_check_float(
            "Please enter the amount of time this bond will "\
                "be repaid over (months): ")
        return house_value, bond_rate, months

    else: return None

#----------------------------------------------------------------------#
''' 
Interest calculations.
'''
def calc_simple_interest(P, r, t):
    return P*(1 + r*t)
def calc_comp_interest(P, r, t):
    return P*math.pow((1 + r),t)
'''
Bond calculation.
'''
def calc_bond_repayment(P, i, n):
    return (i * P)/(1 - math.pow(1 + i,-n))

#----------------------------------------------------------------------#
def investment_main():
    '''
    If "investment" is selected, run this function.
     - Takes user input of the properties of their investment. 
     - Calculates final value of their investment using either
        simple or compound interest (user determined).
     - Displays a summary.
    '''
    deposit, rate, years = user_inputs("investment values")
    dec_rate = rate/100     # % -> decimal conversion

    interest = user_inputs("select investment type")

    if interest == "simple":
        total = calc_simple_interest(deposit, dec_rate, years)
    else:
        total = calc_comp_interest(deposit, dec_rate, years)

    clear_screen()
    print(f"Type of investment: {interest}")
    print(f"Initial deposit: £{deposit}")
    print(f"Interest rate: {rate}%")
    print(f"Length of investment: {years} years")
    print(f"Total value at the end of your investment: £{total}")

#----------------------------------------------------------------------#
def bond_main():
    '''
    If "bond" is selected, run this function.
     - Takes user input of the properties of their bond. 
     - Calculates the monthly cost of repaying the bond.
     - Displays a summary.
    '''
    house_value, bond_rate, months = user_inputs("bond values")

    monthly_bond_rate = bond_rate/1200 # annual (%) -> monthly (decimal)
    monthly_repayment = calc_bond_repayment(
        house_value, monthly_bond_rate, months)
    
    clear_screen()
    print(f"The present value of the house: £{house_value}")
    print(f"The interest rate: {bond_rate}%")
    print(f"Repayment time: {months} months")
    print(f"Calculated monthly repayment: £{monthly_repayment}")

#----------------------------------------------------------------------#
'''
Main program 
    This file contains two programs, `investment_main()` and
    `bond_main()`, which function as different investment/loan 
    calculators.
    This main script takes a user input to select the desired program
    and run it.
'''
if __name__ == "__main__":
    clear_screen()
    program = user_inputs("program select")
    if program == "investment":
        investment_main()
    else:
        bond_main()