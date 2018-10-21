number = 0

low = int(input("Input the starting number of the range"))
high = int(input("Input the ending number of the range"))
for numberCounter in range(low, high, 1):
    number += 1

    if (number%3 == 0 and number%5 == 0):
        print ("FizzBuzz")
    elif (number%5 == 0):
        print ("Buzz")
    elif (number%3 == 0):
        print ("Fizz")
    else:
        print (number)
