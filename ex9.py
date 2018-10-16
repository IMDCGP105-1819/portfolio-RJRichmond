total_cost = 1000000
portion_deposit = 0.25 # 25% needed for a deposit
current_savings = 1.0
annual_salary = 0.0
numberOfMonths = 36
Semi_annual_raise = 0.07
AnnualReturn = 0.04 #r is annual return percentage 4%
portion_saved = 0.0
epsilon = 0.01
bisectionTimes = 0
numberOfMonthsNeeded = 0
guess = 0
remaining = 0

annual_salary = float(input("Enter your starting salary: "))
monthly_salary = (annual_salary / 12)
depositAmount = (total_cost * portion_deposit)


maxValue = 10000
minValue = 0

#guess = (maxValue + minValue)/2
print (current_savings)
print (depositAmount)

savings = current_savings
while abs(current_savings) < depositAmount:
    bisectionTimes += 1
    guess = (maxValue + minValue)/2
    current_savings = 0
    guess = guess/10000
    for month in range(36):
        current_savings += (monthly_salary * guess)
        current_savings += current_savings*(AnnualReturn/12)
        numberOfMonthsNeeded += 1
        #print (current_savings)
        if (numberOfMonthsNeeded / 6) == int(numberOfMonthsNeeded):
            current_savings = (current_savings * Semi_annual_raise)
    #remaining = current_savings - depositAmount
    #print (remaining)
    if current_savings < depositAmount:
        minValue = guess
    elif current_savings > depositAmount:
        maxValue = guess


print ("Best savings rate", guess)
print ("Steps in bisection search", bisectionTimes)
