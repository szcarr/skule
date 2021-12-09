import machine
from machine import Pin, Timer
import random
import utime
lys = True
button2CanBePressed = True
timer = Timer()

potentiometer2 = machine.ADC(28)
potentiometer1 = machine.ADC(26)
potMeterMaxValue = 66000
potMeterLowestValue = 0

pins = [0, 1, 2, 3, 4, 5, 6]
altPins = [16, 17, 18, 19, 20, 21, 22]

button2 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
button1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

primaryList = altPins

ledListe = []
number = [
    8,                          # 8   - 1  Auge
    1 + 32,                     # 33  - 2 Auge
    2 + 8 + 64,                 # 74  - 3 Auge
    1 + 2 + 32 + 64,            # 99  - 4 Auge
    1 + 2 + 8 + 32 + 64,        # 107 - 5 Auge
    1 + 2 + 4 + 16 + 32 + 64    # 119 - 6 Auge
]

individualLed = [
    1,
    2,
    4,
    8,
    16,
    32,
    64,
]

#
#    *   *      64     32
#    * * *      16  8  4
#    *   *       1     2
#
#
#    *          1
#      *           8  
#        *            64

'''
----------------------------------------PATTERNS----------------------------------------
'''

lineRotate = [
    1 + 8 + 32,
    8,
    2 + 8 + 64,
    4 + 8 + 16,
    32 + 8 + 1,
    8,
    64 + 8 + 2,
    16 + 8 + 4,
]
valueToLed = {}

'''
----------------------------------------TING----------------------------------------
'''

def binToTerning(verdi):
    #Verdien er summen av alle leds forhold til posisjon
    for i in range(7):
        maske = verdi & 1 << i
        pinVal = False
        if maske:
            pinVal = True        
        ledListe[i].value(pinVal)
    
def showFace(face):
    binToTerning(number[face - 1])

def showOneLED(ledValue):
    binToTerning(ledValue)

def iterateOverAllNumbersInDice():
    for i in range(len(number)):
        binToTerning(number[i])
        utime.sleep(5)

def lineRotatePattern():
    for y in range(len(lineRotate)):
        binToTerning(lineRotate[y])
        utime.sleep(0.3)

def patternMode():
    while True:
        try:
            print("Doing: showing all numbers on dice")
            iterateOverAllNumbersInDice()
            print("Doing: randomroll")
            for i in range(6):
                showFace(random.randrange(1, len(number)))
                utime.sleep(0.3)
            print("Doing: linerotate")
            for i in range(3):
                lineRotatePattern()
        except KeyboardInterrupt:
            print("Exiting...")
            resetLED()
            break

def turn():
    eachStep = 65535 / 7
    while True:
        currentValue = potentiometer2.read_u16()
        for i in range(7):
            if eachStep * i < currentValue:
                for i in range(i, -1, -1):
                    ledListe[i].value(1)
            if i > 0:
                break
        ledListe[i].value(0)

def variableOneLEDBlinkTest(base):
    while True:
        binToTerning(individualLed[4])
        utime.sleep(potMeterToSeconds(base))
        binToTerning(0)
        utime.sleep(potMeterToSeconds(base))

'''
----------------------------------------POTMETER----------------------------------------
'''

def potMeterToSeconds(base):
    #Base is amount of seconds you want to be divided
    for i in range(100, -1, -1):
        currentValue = readPotmeter2()
        if currentValue > (potMeterMaxValue - 1) / 100 * i:
            return base * ((((potMeterMaxValue - 1) / 100 * i) - potMeterLowestValue) / potMeterMaxValue)

def readPotmeter2():
    return potentiometer2.read_u16()

def readPotmeter1():
    return potentiometer1.read_u16()

'''
----------------------------------------ROULETTE----------------------------------------
'''

'''
----------------------------------------TIMEBASED----------------------------------------
'''

def iterateOverAllNumbersInDiceTime():
    for i in range(len(number)):
        time = potMeterToSeconds()
        binToTerning(number[i])
        utime.sleep(time)

'''
----------------------------------------MEMORYGAME----------------------------------------
'''

def memoryGameMain():
    memoryGameShutDown = False
    computerRolls = []
    userInputs = []
    print("Starting...")
    resetLED()
    utime.sleep(2)
    while True:
        if memoryGameShutDown:
            print("GAME OVER!")
            break
        memoryGameCountdown()
        memoryComputerGenerateNewPattern(computerRolls)
        memoryGameUserInput(computerRolls, userInputs)
        memoryGameShutDown = memoryGameCheckUserInputvsComputer(computerRolls, userInputs, memoryGameShutDown)
        userInputs.clear()

def memoryGameCheckUserInputvsComputer(computerRolls, userInputs, memoryGameShutDown):
    print("Checking if computerRolls is equal to userInputs...")
    if len(computerRolls) is not len(userInputs):
        print("Error: Unequal lists")
        return True

    for i in range(len(computerRolls)):
        if computerRolls[i] is not userInputs[i]:
            print("You failed at index: " + str(i))
            print("Your inputs: " + str(userInputs) + " vs Computer: " + str(computerRolls))
            print("Failed: " + str(userInputs[i]) + " was: " + str(computerRolls[i]))
            return True

    if not memoryGameShutDown:
        print("User passed this round")
        return False
    
            
def memoryGameUserInput(computerRolls, userInputs):
    print("User enter inputs:")
    print(len(computerRolls))
    for i in range(len(computerRolls)):
        print("--" + str(i))
        index = memoryGameUserPotSelectLED()
        userInputs.append(index)
        utime.sleep(1)
    utime.sleep(2)

def memoryComputerGenerateNewPattern(listWithRolls):
    for i in range(len(listWithRolls) + 1):
        binToTerning(0)
        utime.sleep(0.5)
        if i == len(listWithRolls):
            #Makes one new pattern
            #Roll is the index of the LED
            print("Making a new roll")
            roll = random.randrange(0, len(individualLed))
            listWithRolls.append(roll)
            binToTerning(individualLed[roll])
            utime.sleep(1)

        if len(listWithRolls) is not 0:
            print("Printing previous rolls")
            print(i, len(listWithRolls))
            #Goes through list with previously generated rolls
            binToTerning(individualLed[listWithRolls[i]])
            utime.sleep(1)
        
def memoryGameCountdown():
    resetLED()
    print("Showing patterns in ", end="")
    patternList = [
        1 + 4 + 64,
        1 + 4,
        1
    ]
    for i in range(3):
        if i == 2:
            print("Start")
        else: 
            print(3 - i)
        binToTerning(patternList[i])
        utime.sleep(1)
    binToTerning(0)
    utime.sleep(0.5)

def turnOneLedMemoryGame(): #NOT IN USE
    eachStep = potMeterMaxValue / 7
    while True:
        currentValue = readPotmeter2()
        for i in range(7):
            if eachStep * i < currentValue and currentValue < eachStep * (i + 1):
                binToTerning(1<<i)
                if button1.value() == 0:
                    return i

def memoryGameUserPotSelectLED():
    timer.init(period=400, mode=Timer.PERIODIC, callback=timer_cb)
    eachStep = potMeterMaxValue / 7
    while True:
        currentValue = readPotmeter1()
        for i in range(7):
            if eachStep * i < currentValue and currentValue < eachStep * (i + 1):
                ledListe[i].value(lys)
                for n in range(len(ledListe)):
                    if n == i:
                        continue
                    ledListe[n].value(0)
                if button1.value() == 0:
                    return i

def memoryGameUserButtonSelectLED():
    timer.init(period=400, mode=Timer.PERIODIC, callback=timer_cb)
    counter = 0
    while True:
        #print(button2.value(), button2CanBePressed)
        if button2.value() == 0 and button2CanBePressed:
            #print(counter)
            counter += 1
            utime.sleep(0.2)
        if counter > 6:
            counter = 0
        ledListe[counter].value(lys)
        for n in range(len(ledListe)):
            if n == counter:
                continue
            ledListe[n].value(0)
        if button1.value() == 0:
            return counter
        utime.sleep(0.01)

'''
----------------------------------------HELPERS----------------------------------------
'''

def resetLED():
    for i in range(len(ledListe)):
        ledListe[i].value(0)

def addValuesToHashMap(valueToLed):
    for i in range(len(number)):
        valueToLed[number[i]] = primaryList[i]  

def setup():
    for i in range(len(primaryList)):
        ledListe.append(machine.Pin(primaryList[i], machine.Pin.OUT))
        ledListe[i].value(0)

'''
----------------------------------------TIME----------------------------------------

IS USELESS! DO NOT USE
'''

def timer_cb(timer):
    global lys
    lys = not lys

def pinneCallback(pinne):
    print("PC", pinne)
    global button2CanBePressed
    button2CanBePressed = True

def getTimeInHoursMinutesSeconds():
    timeNow = list(str(utime.localtime()).split(", "))
    #Hours is at index 3
    #Minutes is at index 4
    #Seconds is at index 5
    #Returns <hours, minutes, seconds>
    return str(timeNow[3] + ", " + timeNow[4] + ", " + timeNow[5])

def hoursMinutesSecondsToSeconds(obj):
    #Parameter variable should be: example: 11, 22, 43
    obj = str(obj)
    obj = obj.split(", ")
    for i in range(len(obj)):
        obj[i] = int(obj[i])

    objSeconds = obj[2] #Gets seconds

    #Converting hours to seconds
    for i in range(obj[0]):
        objSeconds = objSeconds + obj[0] * 60 * 60

    #Converting minutes to seconds
    for i in range(obj[1]):
        objSeconds = objSeconds + obj[1] * 60

    return int(objSeconds)

def compareTime(obj, objectCompared):
    #obj = now, objectCompared = future
    #Returns true if: now > future else: False
    #Parameters should be raw seconds
    if objectCompared == -1:
        return True

    if obj >= objectCompared:
        return True
    else:
        return False

'''
----------------------------------------INITIALIZER----------------------------------------
''' 

setup()
addValuesToHashMap(valueToLed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=pinneCallback)

'''
----------------------------------------MAIN----------------------------------------
'''

#binToTerning(1 + 2 + 8 + 32 + 64)
#showFace(random.randrange(1, len(number)))
#utime.sleep(3)
#patternMode()
#iterateOverAllNumbersInDice()
#lineRotatePattern()
memoryGameMain()

#getTimeInHoursMinutesSeconds()
resetLED()