my_name = 'Rhys Richmond'
my_age = 18
my_height = 69 #Inches / 175 cm
my_weight = 155 #Pounds
my_eyes = 'Grey'
my_hair = 'Brown/Blonde'
is_heavy = my_weight > 3000

WeightConversion = my_weight / 2.20
HeightConversion = my_height * 2.54

NewWeight = round(WeightConversion, 2)
NewHeight = round(HeightConversion, 2)

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall or {NewHeight} cm tall.")
print(f"He's {my_weight} pounds heavy or {NewWeight} kg heavy.")
print(f"It is {is_heavy} that he is overweight")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, {my_weight} I get {total}")



# is_heavy works by giving a boolean based on if the number is greater then 3000.
#Renaming the variables requires changing it in the print sections too.
