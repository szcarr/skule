

verbose = True
tetris = False
matrix = True

tetrisPrint = True if tetris and verbose else False
matrixPrint = True if matrix and verbose else False

def conditionalPrint(boolean, stringToPrint):
    if boolean:
        print(stringToPrint)