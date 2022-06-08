

verbose = True
wifi = True

wifiPrint = True if wifi and verbose else False

def conditionalPrint(boolean, stringToPrint):
    if boolean:
        print(stringToPrint)