# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:37:18 2021

@author: Andre Merkesdal
"""

#pip install pyfirmata
#https://thecustomizewindows.com/2017/11/use-python-arduino-like-blink-led/

import pyfirmata
import time

'''
-------------------- General --------------------
'''
board = pyfirmata.Arduino('com3')
ledListe = [2,3,4,5,6,7,8,9]

it = pyfirmata.util.Iterator(board)
it.start()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
board.analog[4].enable_reporting()

'''
-------------------- For actualRuntime --------------------
'''

programRuntimeBeforeProgram = 0
programRuntimeAfterProgram = 0

'''
def actualRuntime(isProgramDoneRunning):
    
    'Is called at the START of a fuction with the parameter False
    Is called a second time at the END of a function with the parameter True
    
    Example:
    
    actualRuntime(False)
    for i in range(256):
        bitToLED(i, displayTime)
        time.sleep(timeBeforeNextStep)
    print(actualRuntime(True))   
    '
    try:
        if isProgramDoneRunning:
            programRuntimeAfterProgram = time.process_time()
            return programRuntimeAfterProgram - programRuntimeBeforeProgram
        else:
            programRuntimeBeforeProgram = time.process_time()
    except:
        print("--actualRuntime is always 'False' when its called for the first time in a function")
'''
        
def bitToLED(number, displayTime):
    boardResetLED()
    if number > 255:
        print("--Error number too large. Must be a value from 0 - 255--")
        return -1
    for i in range(8):
        mask = 1<<i
        bit = mask & number
        if bit:
            board.digital[ledListe[i]].write(1)
    time.sleep(displayTime)
    
def boardResetLED():
    for i in range(len(ledListe)):
        board.digital[ledListe[i]].write(0)
        
def calculateRuntime(amountOfLoops, delayInSeconds, howManyTimesDelayIsCalledInOneLoop):
    
    return delayInSeconds * howManyTimesDelayIsCalledInOneLoop * amountOfLoops

def formatSecondsTo(seconds):
    '''
    Returns a string with time !!NOT DONE
    '''
    minutes = 0
    hours = 0
    list = [seconds, minutes, hours]
    
    amountOfUnits = 0
    for i in range(len(list)):
        list[i] = list[i] + amountOfUnits
        amountOfUnits = 0
        try:      
            while list[i] > 60 and len(list) != i - 1:
                list[i] = list[i] - 60
                amountOfUnits = amountOfUnits + 1
        except:
            print("Oops!")
            break
        
    return "Estimated runtime: " + str(list[2]) + " H: " + str(list[1]) + " M: " + str(list[0])+ " S:"
    
def iterateOverAll8Bits(displayTime, timeBeforeNextStep):
    print(formatSecondsTo(calculateRuntime(256, timeBeforeNextStep, 1)))
    programRuntimeBeforeProgram = time.process_time()
    for i in range(256):
        bitToLED(i, displayTime)
        time.sleep(timeBeforeNextStep)
    programRuntimeAfterProgram = time.process_time()
    print('Actual Runtime: ' + str(programRuntimeAfterProgram - programRuntimeBeforeProgram))    
            
def iterateLED(numberOfTimes, delayInSeconds):
    firstRun = True
    for z in range(numberOfTimes):
        for i in range(8):  
            if firstRun:
                firstRun = False
                print(formatSecondsTo(calculateRuntime(numberOfTimes * 8, delayInSeconds, 2)))
            try:  
                print("LED 13 high")
                board.digital[i+2].write(1)
                time.sleep(delayInSeconds)
                
                print("LED 13 low")
                board.digital[i+2].write(0)
                time.sleep(delayInSeconds)
         
            except KeyboardInterrupt:
                print("Bye")
                break
            
def leftStack(lightsOnTime, delaySwitchLED):
    numberOfLEDStoIterateThrough = 8
    try:
        for i in range(8):
                for i in range(numberOfLEDStoIterateThrough):
                    board.digital[ledListe[i]].write(1)
                    time.sleep(lightsOnTime)
                    board.digital[ledListe[i]].write(0)
                board.digital[ledListe[numberOfLEDStoIterateThrough - 1]].write(1)
                numberOfLEDStoIterateThrough = numberOfLEDStoIterateThrough - 1                
                time.sleep(delaySwitchLED)             
    except:
        print("Error in leftstack")
       
def nightRider(numberOfRuns, lightsOnTime, delaySwitchLED):
    print(formatSecondsTo(calculateRuntime(numberOfRuns * 7 * 2 / 2, lightsOnTime + delaySwitchLED, 1)))
    boardResetLED()
    firstRun = True
    x = 0
    y = 7
    nightRiderLEDIteration(x, y, lightsOnTime, delaySwitchLED)
    for i in range(numberOfRuns):
        try:
            x = 1
            y = 6
            for i in range(3): #OK
                nightRiderLEDIteration(x, y, lightsOnTime, delaySwitchLED)
                x = x + 1
                y = y - 1
            x = 2
            y = 5
            for i in range(4):
                if y > 7 or x < 0:
                    continue
                nightRiderLEDIteration(x, y, lightsOnTime, delaySwitchLED)
                x = x - 1
                y = y + 1


        except:
            print("Nightrider fail")
            
def nightRiderLEDIteration(x, y, lightsOnTime, delaySwitchLED):
    board.digital[ledListe[x]].write(1)
    board.digital[ledListe[y]].write(1)
    time.sleep(lightsOnTime)
    board.digital[ledListe[x]].write(0)
    board.digital[ledListe[y]].write(0)
    time.sleep(delaySwitchLED)
        

def potMeterOneLightOn():
    boardResetLED()
    eachStep = 1 / 7
    analogValue = (board.analog[4].read())
    time.sleep(1)
    print("hallo")
    while True:
        for i in range(len(ledListe)):
            board.digital[ledListe[i]].write(0)
            analogValue = (board.analog[4].read())
            if analogValue > (i - 1) * eachStep:
                for y in range(i + 1): #writes everything below as on
                    board.digital[ledListe[y]].write(1)
                    y = y - 1
    
    
def selectPattern():
    boardResetLED()
    
    pattern = [
        [0, 7, 1, 6, 2, 5, 3, 4],
        [0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
    ]
    
    eachStep = 1 / len(pattern) 
    
    while True:
        print("Finding mode")
        boardResetLED()
        time.sleep(2)
        for y in range(len(pattern), 0, -1):
            print(y)
            analogValue = float((board.analog[4].read()))
            if analogValue > y * eachStep:
                for x in range(len(pattern[y - 1])):
                    board.digital[ledListe[x]].write(1)
                break
            
    
'''
---------------------Debug Functions---------------------
'''

def analogReading(amountOfSecondsToRead):
    future = time.process_time() + amountOfSecondsToRead
    now = 0
    while now <= future:
        try:
            analogValue = (board.analog[4].read())
            print(analogValue)
            time.sleep(1)
            now = time.process_time()
        except KeyboardInterrupt:
            print("Bye")
            break
        print("Exiting")
        

def testButton(amountOfSecondsToRead):
    future = time.process_time() + amountOfSecondsToRead
    now = 0
    while now <= future:
        try:
            analogValue = (board.analog[1].read())
            print(analogValue, now)
            time.sleep(1)
            now = time.process_time()
        except KeyboardInterrupt:
            print("Bye")
            break
    print("Exiting")
        
'''
-----------------------Initializer---------------------
'''

boardResetLED()

'''
----------------------Main Program----------------------
'''

delayInSeconds = 2
numberOfTimes = 3
#bitToLED(6, 4)
#iterateLED(numberOfTimes, delayInSeconds)
#leftStack(0.4, 0.1)
#iterateOverAll8Bits(0.1, 0.05) #displayTime, timeBeforeNextStep
#analogReading(4)
#testButton(10)
#nightRider(400, 0.01, 0.002)
#potMeterOneLightOn()
selectPattern()
'''
--------------------MUST EXIT WITH-----------------------
'''
boardResetLED()
board.exit()

