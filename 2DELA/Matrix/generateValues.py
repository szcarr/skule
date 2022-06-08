import random
import readgrid
import tetris
import time

def main():
    print("Thread entered generateValues")
    while True:
        tetris.main()

def generateRandom():
    '''
    Takes a random coordinate then generates a random value in the grid.
    '''
    x = random.randrange(0, 8)
    y = random.randrange(0, 8) 
    value = random.randrange(0, 2)
    coordinates = str(x) + " " + str(y)
    readgrid.gridMapping[coordinates] = value
    readgrid.updateTodo()