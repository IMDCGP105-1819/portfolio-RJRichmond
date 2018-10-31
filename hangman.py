# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    CheckingSecretWord = "".join(get_guessed_word(secret_word,letters_guessed))

    if CheckingSecretWord == secret_word:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    MissingLetters = []
    for i in secret_word:
        if i in letters_guessed:
            MissingLetters.extend(str(i))
        else:
            MissingLetters.extend("_ ")
    return MissingLetters

def TotalScore(NumberOfGuesses,secret_word):
    Score = NumberOfGuesses * len(secret_word)
    return Score

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    Alphabet = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in Alphabet:
            Alphabet.remove(i)

    return " ".join(Alphabet)

def InAlphabet(UserGuess):
    for i in string.ascii_lowercase:
        if UserGuess == i:
            return True
    return False

def isVowel(UserGuess):
    vowels = ['a','e','i','o','u']
    for i in vowels:
        if UserGuess == i:
            return True
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print ("The word contains ", len(secret_word), " letters.")
    print ("You start with 6 Guesses.")
    NumberOfGuesses = 6
    Warnings = 3
    letters_guessed = []
    while (is_word_guessed(secret_word,letters_guessed) == False):
        UserGuess = input(str("Please input a single letter ").lower())
        NumberOfGuesses -= 1
        if UserGuess in letters_guessed:
            print ("You have already Guessed this letter")
            print ("You have",Warnings,"warnings left!")
            NumberOfGuesses += 1
            Warnings -= 1
        elif UserGuess in secret_word:
            print ("You have guessed a letter in the word!")
            NumberOfGuesses += 1
        elif len(UserGuess) != 1 or InAlphabet(UserGuess) == False:
            NumberOfGuesses += 1
            Warnings -= 1
            print ("Please input a single letter from the Alphabet")
            print ("You have",Warnings,"warnings left!")
        else:
            if (isVowel(UserGuess) == True):
                print ("You have guessed a vowel which is not in the word so you lose 2 guesses!")
                NumberOfGuesses -= 1
            else:
                print ("You have guessed a consonast which is not in the word so you lose 1 guess!")
        if NumberOfGuesses <= 0:
            print ("You did not guess the word, it was", secret_word)
            print ("Game Over")
            break

        if Warnings < 1:
            Warnings = 3
            print ("You have used all of your warnings, you will lose 1 guess!")
            NumberOfGuesses -= 1
        letters_guessed.extend(UserGuess)
        print (get_available_letters(letters_guessed))
        print ("".join(get_guessed_word(secret_word, letters_guessed)))
        print ("You have ",NumberOfGuesses," guesses remaining.")
        print ("-----")
    if (is_word_guessed(secret_word,letters_guessed) == True):
        print("You have guessed the word, it was",secret_word,"Well Done!")
        print("Your score for this game was",TotalScore(NumberOfGuesses,secret_word))
        print("Game Over")
secret_word = choose_word(wordlist)
hangman(secret_word)
