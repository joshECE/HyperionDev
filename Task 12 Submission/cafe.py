'''
Task 12
Data Structures - Lists and Dictionaries 

Practical Task --- `cafe.py`
'''

# Menu items available at the cafe
menu = ["Sandwich", "Bagel", "Sausage Roll", "Croissant"]

# Initial stock levels for each menu item
stock = {
    "Sandwich": 20,
    "Bagel": 20,
    "Sausage Roll": 35,
    "Croissant": 30
}

# Prices for each menu item
price = {
    "Sandwich": 3.50,
    "Bagel": 3.75,
    "Sausage Roll": 2.45,
    "Croissant": 1.95
}

# Initialize the total value of the cafe's stock
total_stock = 0

# Calculate the total value of the stock
for item in menu:
    total_stock += stock[item] * price[item]

# Display the total value
print(f"Total value of the stock: £{total_stock}")
