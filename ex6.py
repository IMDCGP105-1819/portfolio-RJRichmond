
Name = input ("What is your name?")
Age =  int(input ("How old are you?"))
Height = int(input ("What is your height in cm?"))
Weight = int(input("How much do you weight in Kg?"))
EyeColour = input ("What colour eyes to you have?")
HairColour = input ("What colour hair do you have?")

WeightHealth = Height - Weight
#AverageHeight = range(162,190)

if (Age < 17 ):
    print ("You are a very young person")
elif (18 < Age <= 45 ):
    print ("You are in your prime")
else:
    print ("You are a slightly older, wise person")


if (95 < WeightHealth <= 105):
    print ("You are normal weight for your height")
else:
    print ("You are at an unhealthy weight")

if (162 <= Height <= 190):
    print ("You are Average Height")
elif ( 191 <= Height):
    print ("You are pretty tall")
else :
    print ("You might be slightly smaller then average")
