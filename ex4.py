myName = 'Rhys Richmond'
myAge = 18
myHeight = 69 #Inches
myWeight = 155 #Pounds
myEyes = 'Grey'
myHair = 'Brown/Blonde'
# is_heavy works by giving a boolean based on if the number is greater or lower then 3000 .
is_heavy = my_weight > 3000

# I have added variables to calculate the conversions and then used round to make the numbers to 2 decimal places so it looks neat.
WeightConversion = my_weight / 2.20
HeightConversion = my_height * 2.54

NewWeight = round(WeightConversion, 2)
NewHeight = round(HeightConversion, 2)

print(f"Let's talk about {myName}.")
print(f"He is {myHeight} inches tall or {NewHeight} cm tall.")
print(f"He's {myWeight} pounds heavy or {NewWeight} kg heavy.")
print(f"It is {is_heavy} that he is overweight")
print(f"He's got {myEyes} eyes and {myHair} hair.")

total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight}, {myWeight} I get {total}")


# I have changed the variable names to my prefered way of typing variables which is camel case.
