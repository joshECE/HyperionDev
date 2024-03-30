'''
Task 14
IO Operations - Input 

Practical Task --- `dob_task.py`

'''

# Empty lists to store names and dates
names = []
dates = []


with open("DOB.txt","r") as file:   
    for line in file:
        # Split the line into a list of words
        word_list = line.split()

        # Extract names and dates from the line
        name_string = " ".join(word_list[:2])
        date_string = " ".join(word_list[2:])

        # Append the name and date to their respective lists
        names.append(name_string)
        dates.append(date_string)

# Join the names and dates lists into formatted strings
names_string = "\n".join(names)
dates_string = "\n".join(dates)
        
# Print the formatted output for names and dates
print(f"NAME\n{names_string}\n")
print(f"BIRTHDATE\n{dates_string}")
