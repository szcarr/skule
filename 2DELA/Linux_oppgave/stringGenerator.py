import string
import random

letters = string.ascii_letters
numbers = string.octdigits
symbols = string.punctuation

def generateRandomString(**kwargs):

    '''
    Returns a randomly generated string

    Kwargs expected is;
    length = 14 #Determines the length of the generated string
    '''

    lengthOfString = 8

    for key in kwargs.keys():
        if key == "length":
            lengthOfString = kwargs.get(key)

    results = ""
    
    for i in range(lengthOfString):
        choice = random.randrange(0, 3)
        if choice == 0: #Chooses letters
            n = random.randrange(0, len(letters))
            results = results + letters[n]
        elif choice == 1: #Chooses a digit
            n = random.randrange(0, len(numbers))
            results = results + numbers[n]
        elif choice == 2: #Chooses a symbol
            n = random.randrange(0, len(symbols))
            results = results + symbols[n]

    return results