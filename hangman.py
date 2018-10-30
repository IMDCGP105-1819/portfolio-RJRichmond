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
    NumberOfLettersInBoth = 0
    for i in letters_guessed:
        if i in secret_word:
            NumberOfLettersInBoth += 1
    if NumberOfLettersInBoth == len(secret_word):
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
    return " ".join(MissingLetters)


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
    letters_guessed = []
    while (is_word_guessed(secret_word,letters_guessed) == False):
        UserGuess = input(str("Please input a single letter ").lower())
        #letters_guessed.extend(UserGuess)
        NumberOfGuesses -= 1
        if UserGuess in letters_guessed:
            print ("You have already Guessed this letter")
        elif UserGuess in secret_word:
            print ("You have guessed a letter in the word!")
            NumberOfGuesses += 1
        else:
            print ("The letter you have guessed is not in the word")
        if NumberOfGuesses <= 0:
            print ("You did not guess the word, it was ", secret_word)
            print ("Game Over")
            break
        letters_guessed.extend(UserGuess)
        print (get_available_letters(letters_guessed))
        print (get_guessed_word(secret_word, letters_guessed))
        print (NumberOfGuesses)
secret_word = choose_word(wordlist)
hangman(secret_word)
