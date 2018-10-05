total_cost = 0.0
portion_deposit = 0.0
current_savings = 0.0
annual_salary = 0.0

r = 0.04 #r is annual return percentage 4%
portion_saved = 0.0

monthlyReturn = (current_savings * r) / 12
monthly_salary = (annual_salary / 12)
monthlySaved = (monthly_salary * portion_saved)

totalPerMonth = (monthlySaved + monthlyReturn)

annual_salary = float(input("Please input your annual salary"))
portion_saved = float(input("Please input the percentage of money you will save per month"))
total_cost = float(input("Please input the cost of your dream home"))

numberOfMonthsNeeded = (total_cost / totalPerMonth)

print ("Number of months needed:",numberOfMonthsNeeded)
