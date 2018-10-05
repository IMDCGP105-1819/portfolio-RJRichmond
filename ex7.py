total_cost = 0.0
portion_deposit = 0.20 # 20% needed for a deposit
current_savings = 0.0
annual_salary = 0.0

r = 0.04 #r is annual return percentage 4%
portion_saved = 0.0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# This section takes the values the user inputted and then uses them to work out the monthly salary, deposit amount, total saved per month and what their return on the interest is.
monthly_salary = (annual_salary / 12)
depositAmount = (total_cost * portion_deposit)
print (depositAmount)
current_savings = (monthly_salary * portion_saved)
monthlyReturn = (current_savings * r/12)


#This then works out the total amount being saved a month and the number of months needed to reach the goal.
totalPerMonth = (current_savings + monthlyReturn)
print (totalPerMonth)
numberOfMonthsNeeded = (depositAmount / totalPerMonth)

print ("Number of months: ",numberOfMonthsNeeded)
