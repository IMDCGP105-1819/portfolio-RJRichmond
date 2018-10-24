def Hotel_cost(nights):
    return nights * 70

def plane_ticket(city, PlaneClass):
    if (city == "New york"):
        TotalPlaneCost = 2000 * PlaneClass
        PlaneClass = TotalPlaneCost
        return PlaneClass

    elif (city == "Auckland"):
        TotalPlaneCost = 790 * PlaneClass
        PlaneClass = TotalPlaneCost
        return PlaneClass
    elif (city == "Venice"):
        TotalPlaneCost = 154 * PlaneClass
        PlaneClass == TotalPlaneCost
        return PlaneClass
    elif (city == "Glasgow"):
        TotalPlaneCost = 65 * PlaneClass
        PlaneClass == TotalPlaneCost
        return PlaneClass
    else:
        return

def Rental_car(days):
    totalRentalCarCost = days * 30
    if (days > 7):
        days = totalRentalCarCost -50
        return days
    elif ( 7 > days >= 3):
        days = totalRentalCarCost -30
        return days

def total_cost(int):
    nights = Hotel_cost(int(input("How many nights are you staying? ")))
    city = plane_ticket(city = str(input("What city are you traveling to? ")),PlaneClass = float(input("Please enter the multiplier of the class you will be flying ")) )
    days = Rental_car(days = int(input("How many days are you going to be there ")))
    total_cost = nights + city + days
    return total_cost

print ("Destinations you can travel to : New york, Auckland, Venice and Glasgow. ")
print ("Make sure to input exactly as they appear! ")
print ("Avaliable classes: Economy = 1, Premium Economy = 1.3, Business Class = 1.6 and First Class = 1.9 ")
price = total_cost(int)
print ("It will cost you", price)
