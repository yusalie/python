# Defines function for cost of nights
def hotel_cost(nights):
    # Returns calculation
    return print(nights*140)

#Gets user input
hotel_cost(int(input("nights:\n")))

#Defines function for plane ride
def plane_ride_cost(place):

#Decision tree
    if place.lower() == "cape town":
        print("Cape Town: 2500")
    elif place.lower() == "durban":
        print("Durban: 2300")
    elif place.lower() == "jhb":
        print("JHB:2000")
    elif place.lower() == "bfn":
        print("BFN:1800")


#List of cities
cities = ["cape town", "Durban", "JHB", "BFN"]

#prints cities
print(cities)

#Gets user input
plane_ride_cost(input("Select city\n").lower())

#Defines function
def rental_car(days):
    
    #Calculates price
    price_calc = days*40
    
    #Prints first amount
    print("the orignal price ", price_calc)
    
    #Desicion tree
    if days >= 7:
        price_calc -= 40
    elif days <= 3:
        price_calc -= 20

    #Outputs final result
    return print("the discounted amount is: ", price_calc)

#Gets user input
rental_car(int(input("how many days would you like the car:\n")))

def trip_cost():
    trip_tot = rental_car
    return print(trip_tot)
