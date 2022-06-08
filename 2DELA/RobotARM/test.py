import urx

rob = urx.Robot("192.168.1.116")

defaultstance = [0.6463298603973687, -0.2080601348485878, 0.6643070693930722, -3.0429026978061406, 0.6944244466872044, 0.08256847108677146]

v = 0.05
a = 0.1

#Movements are in centimeters as we divide by 100 in the movel commands 
def defaultStance():
    #rob.movej((696, -146, 226, 1.59, -2.6, -0.041), acc=0.1, vel=0.05, relative=False)
    rob.movel(defaultstance, acc=a, vel=v)

def main():
    defaultStance()

def printState():
    try:
        while True:
            print(rob.getl())
    except:
        rob.close()

main()