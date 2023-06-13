print("Type where you would like to go from the following;\nNew York, London or Paris: ")

location = ['NEW YORK', 'LONDON', 'PARIS']

while True: #loop until correct input
    city_flight = input("Choose where you would like to fly to: ")
    city_flight = city_flight.upper() #error handling, changes input to uppercase before searching
    if city_flight in location:
        break
    else:
        print("\nInvalid input. Please try again.\n")

num_nights = int(input("How many nights are you staying?: "))


while True: #loop until correct input
    rental_days = int(input("How many days will you be renting a car for?: "))
    if rental_days <= num_nights:
        break
    else:
        print("You're renting a car more nights than you will be staying! Please try again.\n")


def plane_cost(city_flight):
    if city_flight in location[0]: #New York
        flight = 650

    elif city_flight in location[1]: #London
        flight = 180

    elif city_flight in location[2]: #Paris
        flight = 525

    else:
        flight = 0

    return flight


def hotel_cost(num_nights):
    if city_flight in location[0]: #New York
        hotel = 120

    elif city_flight in location[1]: #London
        hotel = 130

    elif city_flight in location[2]: #Paris
        hotel = 100

    else:
        hotel = 0

    h_cost_total = hotel * num_nights #cost of stay multiplied by how many nights

    return h_cost_total #total cost of hotel

def car_rental(rental_days):
    if city_flight in location[0]: #New York
        car = 35

    elif city_flight in location[1]: #London
        car = 50

    elif city_flight in location[2]: #Paris
        car = 42

    else:
        car = 0

    car_cost_total = car * rental_days #cost of car rental (for 1 day) multiplied by days renting

    return car_cost_total #car rental price total

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total

#print all details of holiday prices and total cost of holiday
print("Holiday Details:")
print("City Flight:", city_flight)
print("Number of Nights:", num_nights)
print("Number of Rental Days: £", rental_days)
print("Hotel Cost: £", hotel_cost(num_nights))
print("Plane Cost: £", plane_cost(city_flight))
print("Car Rental Cost: £", car_rental(rental_days))
print("Total Holiday Cost: £", holiday_cost(hotel_cost, plane_cost, car_rental))