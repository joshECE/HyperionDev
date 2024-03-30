'''
Task 16

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
Error caused by incorrect user input.
'''
def display_error():
    print("Error: Invalid input. Please try again.")


cities = [
    "Tokyo",
    "New York City",
    "Paris",
    "London",
    "Beijing",
    "Sydney",
    "Rio de Janeiro",
    "Cape Town",
    "Dubai",
    "Mumbai",
    "Toronto",
    "Berlin",
    "Seoul",
    "Moscow",
    "Buenos Aires",
    "Bangkok",
    "Istanbul",
    "Los Angeles",
    "Rome",
    "Stockholm",
]

cities_prices_data = {
    "tokyo": [800, 150, 50],
    "new york city": [600, 200, 80],
    "paris": [150, 120, 60],
    "london": [0, 150, 40],  # Assuming the flight from London is the 
    # reference point with a cost of 0
    "beijing": [900, 80, 30],
    "sydney": [1200, 180, 70],
    "rio de janeiro": [1000, 90, 45],
    "cape town": [800, 100, 35],
    "dubai": [300, 120, 50],
    "mumbai": [700, 80, 25],
    "toronto": [500, 150, 55],
    "berlin": [100, 100, 45],
    "seoul": [1000, 110, 40],
    "moscow": [250, 80, 35],
    "buenos aires": [1100, 95, 50],
    "bangkok": [800, 70, 25],
    "istanbul": [200, 90, 40],
    "los angeles": [700, 180, 60],
    "rome": [120, 130, 55],
    "stockholm": [80, 120, 50],
}

def get_city():
    city_input = None
    while city_input not in cities_prices_data:
        city_input = input(
            "Please enter a holiday destination from the list: ")
        city_input = city_input.lower()
        clear_screen()
        display_description()
        display_error()
    
    return city_input

def get_int(input_message):
    clear_screen()
    while True:
        try:
            return int(input(input_message))
        except ValueError:
            clear_screen()
            display_error()

def get_inputs():
    city_flight = get_city()

    num_nights = (
        get_int("Please enter the number of nights you will stay in "\
                "a hotel: ")
        )
    rental_days = (
        get_int("Please enter the number of days you will rent a car: ")
        )
    return city_flight,num_nights,rental_days

def hotel_cost(num_nights,city_prices):
    return num_nights*city_prices[1]

def plane_cost(city_prices):
    return city_prices[0]

def car_rental(rental_days,city_prices):
    return rental_days*city_prices[2]

def holiday_cost(hotel_cost,plane_cost,car_rental):
    return sum(hotel_cost,plane_cost,car_rental)

def display_description():
    clear_screen()
    description = (
"""You are from London and you would like to go on holiday. In this
program you will select a holiday destination, the number of nights
you will be staying in a hotel and the number of nights you will be
renting a car. The program will then show you a summary of the cost
of your holiday, including the total cost.
"""
    )
    print(description)

    print("List of holiday options:\n")
    print(", ".join(cities))


display_description()
print(get_inputs())
city_flight, num_nights, rental_days = get_inputs()

    
    
    



