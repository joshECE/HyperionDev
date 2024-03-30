'''
Practical Task 2 --- `replace.py`

Psuedocode:

- Declare a variable `sentence` containing the string in the assignment.
- Reassign `sentence` using `replace()` to replace every '!' with ' ' and print.
- Reassign `sentence` using `upper()` to make the sentence upper case and print.
- Reverse `sentence` and print.

'''

# Declare the `sentence` as a string.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace the "!" in `sentence` with " ".
sentence = sentence.replace("!"," ")

# Print the updated string.
print(sentence)

# Change the sentence to all upper case.
sentence = sentence.upper()

# Print the updated string.
print(sentence)

# Reverse the string and print.
print(sentence[::-1])