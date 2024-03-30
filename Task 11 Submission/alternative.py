'''
Practical Task 1 --- `alternate.py`

'''

# Accepts user input
input_string = input()

# Process the characters in the input string, alternating between upper
# and lower case
output_string1 = []
for i in range(len(input_string)):
    current_char = input_string[i]
    if i % 2 == 0:
        output_string1.append(current_char.upper())
    else:
        output_string1.append(current_char.lower())
output_string1 = "".join(output_string1)

# Split the input string into words and alternate the case of each word
output_string2 = input_string.split()
for i in range(len(output_string2)):
    if i % 2 == 0:
        output_string2[i] = output_string2[i].lower()
    else:
        output_string2[i] = output_string2[i].upper()
output_string2 = " ".join(output_string2)

# Display the results
print(output_string1)
print(output_string2)