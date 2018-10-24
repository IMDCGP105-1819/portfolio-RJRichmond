def Hotel_cost(nights):
    #nights = int(input("How many nights are you staying?"))
    #HotelTotalCost = nights * 70
    nights = nights * 70

def plane_ticket(city, PlaneClass):
    #print ("Destinations you can travel to : New york, Auckland, Venice and Glasgow.")
    #print ("Make sure to input exactly as they appear!")
    #city = int(input("What city are you traveling to?"))

    #print ("Avaliable classes: Economy = 1, Premium Economy = 1.3, Business Class = 1.6 and First Class = 1.9")
    #PlaneClass = float(input("Please enter the multiplier of the class you will be flying"))
    if (city == "New york"):
        TotalPlaneCost = 2000 * PlaneClass
        PlaneClass = TotalPlaneCost
    elif (city == "Auckland"):
        TotalPlaneCost = 790 * PlaneClass
        PlaneClass = TotalPlaneCost
    elif (city == "Venice"):
        TotalPlaneCost = 154 * PlaneClass
        PlaneClass = TotalPlaneCost
    elif (city == "Glasgow"):
        TotalPlaneCost = 65 * PlaneClass
        PlaneClass = TotalPlaneCost
    else:
        return

def Rental_car(days):
    #days = int(input("How many days are you going to be their"))

    totalRentalCarCost = days * 30

    if (days > 7):
        days = totalRentalCarCost -50
    elif ( 7 > days >= 3):
        days = totalRentalCarCost -30

def total_cost (city, days, nights):
    #Hotel_cost();
    #plane_ticket();
    #Rental_car();
    total_cost = nights + PlaneClass + days
    print ("It would cost", total_cost)

nights = int(input("How many nights are you staying? "))
Hotel_cost(nights);
print ("Destinations you can travel to : New york, Auckland, Venice and Glasgow. ")
print ("Make sure to input exactly as they appear! ")
city = str(input("What city are you traveling to? "))

print ("Avaliable classes: Economy = 1, Premium Economy = 1.3, Business Class = 1.6 and First Class = 1.9 ")
PlaneClass = float(input("Please enter the multiplier of the class you will be flying "))
plane_ticket(city, PlaneClass);
days = int(input("How many days are you going to be there "))
Rental_car(days);
total_cost(city, days, nights);
