'''
Task 9:
Defensive Programming - Error Handling
Practical Task 2 - `logic.py`

'''

'''
I have been working on a fun problem to convert an integer to a roman
numeral. Last week I came up with a solution and after testing it with
a few inputs, I believed it was working. However, after trying a larger 
amount of numbers, I realized that the conversion would occasionally
be incorrect. Here is my original solution:
'''

dec_value = 10


values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]


numeral = []
while dec_value != 0:
    for i in range(13):
        if dec_value - values[i] >= 0:
            dec_value -= values[i]
            numeral.append(symbols[i])
            print(values[i])

numeral = "".join(numeral)

print(f"Original code output: {numeral}")

'''
Try setting `dec_value` to 20 for the original code, the output 
will be "XIXI" when it should be "XX". 

In the corrected code, a break statement is added in the for loop
to prevent it appending a numeral smaller than the current numeral,
when the same numeral should be repeated twice. 
'''


dec_value = 10

numeral = []
while dec_value != 0:
    for i in range(13):
        if dec_value - values[i] >= 0:
            dec_value -= values[i]
            numeral.append(symbols[i])
            break

numeral = "".join(numeral)

print(f"Fixed code output: {numeral}")