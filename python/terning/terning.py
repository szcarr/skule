import machine
import random
import utime

pins = [0, 1, 2, 3, 4, 5, 6]
ledListe = []
number = [
    1,                          # 1 - 1 Auge
    32 + 2,                     # 34 - 2 Auge
    1 + 8 + 64,                 # 73 - 3 Auge
    1 + 2 + 32 + 64,            # 99 - 4 Auge
    1 + 2 + 8 + 32 + 64,        # 107 - 5 Auge
    1 + 2 + 4 + 16 + 32 + 64    # 119 - 6 Auge
    ]
#
#    *   *      1      2
#    * * *      4  8  16
#    *   *      32    64
#
#
#    *          1
#      *           8  
#        *            64

valueToLed = {}

def binToTerning(verdi):
    #Verdien er summen av alle leds forhold til posisjon
    for i in range(7):
        mask = verdi & 1 << i
        pinVal = False
        if mask:
            pinVal = True        
        ledListe[i].value(pinVal)
    

def setup():
    for i in range(len(pins)):
        ledListe.append(machine.Pin(pins[i], machine.Pin.OUT))
        ledListe[i].value(0)


def lystest():
    for i in range(2):
        print("")

def asopdkaosdk():
    for i in range(len(number)):
        binToTerning(number[i])
        utime.sleep(1)

def rollRandomNumber():
    return random.randrange(1, 7)

def terningDisplay(numberToDisplay):
    for i in range(len(ledListe)):
        if numberToDisplay == 1:
            print("")
            
def resetLED():
    for i in range(len(ledListe)):
        ledListe[i].value(0)

def addValuesToHashMap(valueToLed):
    for i in range(len(number)):
        valueToLed[number[i]] = pins[i]
'''
--------------------MAIN--------------------
'''

setup()
addValuesToHashMap(valueToLed)
#binToTerning(1 + 2 + 8 + 32 + 64)
asopdkaosdk()
