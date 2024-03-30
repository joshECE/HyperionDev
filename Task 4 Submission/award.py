"""
Practical Task 1 --- `award.py`

Psuedocode:

- Declare variables for swimming, cycling and running times with the 
input of a user (converted to int).

- Add these values together and save to a new variable `total_time`.

- Print the the total triathlon time.

- Print "Award received: " to be followed by the relevant award.

- If the total time is less than 101 minutes:
    The award is "Provincial Colours".
    ELSE IF the total time is less than 106 minutes:
        The award is "Provincial Half Colours".
        ELSE IF the total time is less than 111 minutes:
            The award is "Provincial Scroll".
            ELSE:
                No award.

"""

# Gather user inputs for different section times, convert to 
# integer and save to variables. 
swimming_time = int(input("Swimming time: "))
cycling_time = int(input("Cycling time: "))
running_time = int(input("Running time: "))

# Sum the times together to determine total race time and save to 
# `total_time`.
total_time = swimming_time + cycling_time + running_time

# Print the total race time.
print("Triathlon total time: " + str(total_time))

# Print "Award received: " followed by the relevant award.
print("Award received: ",end="")

# If total time is less than 101 mins: print "Provincial Colours".
if total_time < 101:
    print("Provincial Colours")
# If total time is faster than 106 mins but slower than 100 mins:
# print "Provincial Half Colours".
elif total_time < 106:
    print("Provincial Half Colours")
# If total time is faster than 111 mins but slower than 105 mins:
# print "Provincial Scroll".
elif total_time < 111:
    print("Provincial Scroll")
# If total time is slower than 111 mins: print "No Award".
else:
    print("No award")