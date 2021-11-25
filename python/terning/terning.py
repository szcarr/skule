import machine
import random
import utime

pins = [0, 1, 2, 3, 4, 5, 6]
ledListe = []
number = [
    8,                          # 8   - 1  Auge
    1 + 32,                     # 33  - 2 Auge
    2 + 8 + 64,                 # 74  - 3 Auge
    1 + 2 + 32 + 64,            # 99  - 4 Auge
    1 + 2 + 8 + 32 + 64,        # 107 - 5 Auge
    1 + 2 + 4 + 16 + 32 + 64    # 119 - 6 Auge
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
'''
----------------------------------------HELPERS----------------------------------------
'''

def resetLED():
    for i in range(len(ledListe)):
        ledListe[i].value(0)

def addValuesToHashMap(valueToLed):
    for i in range(len(number)):
        valueToLed[number[i]] = pins[i]  

def setup():
    for i in range(len(pins)):
        ledListe.append(machine.Pin(pins[i], machine.Pin.OUT))
        ledListe[i].value(0)      

'''
----------------------------------------INITIALIZER----------------------------------------
'''

setup()
addValuesToHashMap(valueToLed)

'''
----------------------------------------MAIN----------------------------------------
'''

#binToTerning(1 + 2 + 8 + 32 + 64)
#showFace(random.randrange(1, len(number)))
#utime.sleep(3)
#patternMode()
#iterateOverAllNumbersInDice()
for i in range(20):
    lineRotatePattern()
resetLED()