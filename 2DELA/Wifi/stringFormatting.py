import string

letters = string.ascii_letters
numbers = string.octdigits
symbols = string.punctuation

def removeSpacesBeforeAndAfterString(string):
    '''
    s = String to be formatted
    Returns s but formatted 
    '''

    firstCharIndex = -1
    lastCharIndex = -1
    hasNotFoundFirstChar = True
    for c in range(len(string)):
        if string[c] == " ":
            continue
        elif hasNotFoundFirstChar and string[c] != " ":
            hasNotFoundFirstChar = False
            firstCharIndex = c
        elif string[c] != " ":
            lastCharIndex = c

    #print(firstCharIndex, lastCharIndex, string[firstCharIndex], string[lastCharIndex])

    newString = ""
    for i in range(firstCharIndex, lastCharIndex):
        newString = newString + string[i]

    return newString

#print(removeSpacesBeforeAndAfterString("      asdf l,df      "))