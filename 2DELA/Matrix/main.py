import threading
import time
import readgrid
import generateValues
import matrix

threads = []
amountOfThreads = 2

width, height = 8, 8

def setup():
    baseValue = 0 #is Off
    for x in range(width):
        for y in range(height):
            coordinates = str(x) + " " + str(y)
            readgrid.gridMapping[coordinates] = baseValue

def run():
    for i in range(amountOfThreads):
        print(i)
        if i == 0: #Goes to update
            t = threading.Thread(target=matrix.setLED)
            t.daemon = True
            threads.append(t)
        elif i == 1:
            t = threading.Thread(target=generateValues.main)
            t.daemon = True
            threads.append(t)
    print(len(threads))
    for i in range(len(threads)):
        threads[i].start()
        time.sleep(1)

    for i in range(len(threads)):
        threads[i].join()

setup()
run()