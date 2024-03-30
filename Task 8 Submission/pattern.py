'''
Practical Task 1 --- `pattern.py`

'''

star_string = "*****"

# Print different slices of `star_string` string depending on the 
# value of `i`. 
for i in range(1,10):
    if i < 5:
        print(star_string[:i])
    else:
        print(star_string[i%5:])