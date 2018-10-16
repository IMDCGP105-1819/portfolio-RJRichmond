total_cost = 0.0
portion_deposit = 0.20 # 20% needed for a deposit
current_savings = 0.0
annual_salary = 0.0
numberOfMonthsNeeded = 0.0
#numberOfMonthsUntilRaise = 0.0

r = 0.04 #r is annual return percentage 4%
portion_saved = 0.0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
Semi_annual_raise = float(input("Enter a Semi annual raise ammount: "))


# This section takes the values the user inputted and then uses them to work out the monthly salary, deposit amount, total saved per month and what their return on the interest is.
monthly_salary = (annual_salary / 12)
depositAmount = (total_cost * portion_deposit)



#This loop runs when the savings is less then the deposit, the loop adds the monthly savings, the interest and then it adds 1 to the month variable, until the amount is met.

while current_savings < depositAmount :
    current_savings += (monthly_salary * portion_saved)
    current_savings += current_savings*(r/12)
    numberOfMonthsNeeded += 1
    #numberOfMonthsUntilRaise += 1
    if (numberOfMonthsNeeded / 6) == int(numberOfMonthsNeeded):

        current_savings = (current_savings * Semi_annual_raise)
        #print ("A raise happened")

print ("Number of months: ",numberOfMonthsNeeded)
