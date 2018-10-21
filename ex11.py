from random import randint

NumberToGuess = randint(0,100)


def GuessingGame(int):
    TimesGuessed = 0
    while True:
        User = int(input("Please guess a number between 1-99 "))
        TimesGuessed += 1
        if User > NumberToGuess:
            print ("You have guess too high")
        elif User < NumberToGuess:
            print ("You have guessed too low")
        elif User == NumberToGuess:
            print ("You have guessed the correct number")
            print ("You guess",TimesGuessed,"Times!")
            break


GuessingGame(int);
