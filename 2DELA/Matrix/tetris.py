import time

import matrix
import geometry
import movement
import prints

def main():
    while True:
        newPos = geometry.line()
        for s in range(6):
            newPos = movement.shift(newPos, 3, 1)
            newPos = movement.shift(newPos, 2, 1)
            for x in range(len(newPos)):
                coordinates = str(newPos[x][0]) + " " + str(newPos[x][1])
                matrix.grid[coordinates] = str(newPos[x][2])
                prints.conditionalPrint(prints.tetrisPrint, "Coordinates are: " + coordinates)
                time.sleep(1)

        