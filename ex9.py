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
failsafe = 0

annual_salary = float(input("Enter your starting salary: "))
monthly_salary = (annual_salary / 12)
depositAmount = (total_cost * portion_deposit)


maxValue = 10000
minValue = 0
#savings = current_savings
#guess = (maxValue + minValue)/2
guess = (maxValue + minValue)/2

while True:
    #current_savings = savings
    failsafe += 1
    bisectionTimes += 1
    guess = round((maxValue + minValue)/2,2)
    portion_saved = guess/10000

    for month in range(36):
        current_savings += (monthly_salary * portion_saved)
        current_savings += current_savings*(AnnualReturn/12)
        numberOfMonthsNeeded += 1
        #print (numberOfMonthsNeeded / 6)
        if (numberOfMonthsNeeded%6) == 0:
            #print ("This actually happen")
            monthly_salary += (monthly_salary * Semi_annual_raise)
    #print(current_savings)
    if current_savings > depositAmount:
        maxValue = guess
        current_savings = 1.0
        numberOfMonths = 0
        monthly_salary = (annual_salary / 12)

        if failsafe > 100:
            break
        if (current_savings < 250100 and current_savings > 249900):
            print("break")
    elif (current_savings < 250100 and current_savings > 249900):
        break

    elif current_savings < depositAmount:
        minValue = guess
        current_savings = 1.0
        numberOfMonths = 0
        monthly_salary = (annual_salary / 12)
        #guess = guess*10000


print ("Best savings rate", portion_saved)
print ("Steps in bisection search", bisectionTimes)
