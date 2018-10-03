# Here the variables are being created and are assigned values.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Then some new variables are being created using the previously created variables, for example "cars_not_driven" is taking the
# cars variable and subtracting it from the drivers variable.
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

#The error is due to the variable name not being inputted properly.
#The difference between using a float and a interger is that a float will print as a decimal and a interger won't.
