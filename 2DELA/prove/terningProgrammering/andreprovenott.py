import machine
import random
import utime

primaryList = [16, 17, 18, 19, 20, 21, 22] #mine pins


# DET SOM VAR FEIL:
# MØNSTER terning trill 2 og 3 var feil

#Det eg endra
# endra raskt på tala i valueOfPins har lagt kommentara der
#la til setup funksjonen som legger til alle pinsa i ei liste
#endra også pinsa i forhold til mitt kretskort
#Ellers var alt perfekt

ledListe = []
valueOfPins = [
    8,
    2 + 64,  #Måtte endre 32 til 64
    1 + 8 + 32, #Måtte endre 64 til 32
    1 + 2 + 32 + 64,
    1 + 2 + 8 + 32 + 64,
    1 + 2 + 4 + 16 + 32 + 64
]

def setup():
    for i in range(len(primaryList)):
        ledListe.append(machine.Pin(primaryList[i], machine.Pin.OUT))
        ledListe[i].value(0)

def rollRandomdDice():
    amountOfRolls = random.randrange(2, 20)
    listWithRolls = []
    print(amountOfRolls)
    for n in range(amountOfRolls): #Adds rolls to list a roll is a number that can be displayed on a dice
        roll = random.randrange(0, 6)
        listWithRolls.append(roll)

    print(listWithRolls)

    while True:
        for l in range(len(listWithRolls)):
            # trekker tal frå listWithRolls lista med index l
            for i in range(7):
                #Går igjennom for kvart einaste bit i 
                if valueOfPins[listWithRolls[l]] & 1 << i:
                    # går inn i listWithrolls og hentar ut terning trill index so brukar eg det som indexen i valueOfpins
                    ledListe[i].value(1)
            utime.sleep(1) # på i eit sekund
            for o in range(len(ledListe)):
                ledListe[o].value(0) #setter alle pinsa til 0
            utime.sleep(1) #av i eit sekund
        utime.sleep(5) #resettar sleepa i 5 sekund

setup()
rollRandomdDice()

#    while True:
      #  for l in range(len(listWithRolls)):
     #       for i in range(7):
    #            ledListe[i].value(0)
   #             if valueOfPins[listWithRolls[roll]] & 1 << i:
  #                  ledListe[i].value(1)
 #           utime.sleep(1)
#        utime.sleep(5)