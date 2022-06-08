#04:BD:88:68:8D:E0 I GANGEN

'''
For switch finn mac addressa på switchen:
00:1D:B3:F0:B3:80
sudo nast -m | grep "B3:80"
Finn ip 
telnet <ip>
Sjå https://github.com/jarleven/NetworkHOWTO/blob/master/Switch/HPProCurve.md
Ctrl+f Configure Power over

https://192.168.1.151:4343 er ip på AP i gangen
https://192.168.1.139:4343 er home

'''

#Bruk webbrowser til å logge inn på AP-et
#Finne ka port AP brukar for å komme inn på web gui
#Potensielt 192.168.1.165

import os
import time

import prints
import stringFormatting
import fileHandling as fh

password = "beltevogn"

listeMedSSIDNamn = [
    "Beltevogn_printer",
    "Beltevogn_home"
]

DEFAULTSSIDNAMN = "Beltevogn"

currentlySelectedNetwork = None 

def main(**kwargs):
    '''
    kwargs = 
    update #amount of seconds to update and scan for anew network
    threshold = 
    '''

    update = 5
    threshold = 0

    for k in kwargs.keys():
        if "update" == k:
            update = kwargs.get(k)
        elif "threshold" == k:
            threshold = kwargs.get(k)

    print("Wifi program setup with: update = " + str(update) + " threshold = " + str(threshold))

    while True:
        lst, bn = filterByQuality(getWifi(), threshold)
        print("Currently connected to: %s." % (str(currentlySelectedNetwork)))
        changeConnection(bn)
        time.sleep(update)

def getWifi():
    output = str(os.popen('sudo iwlist wlan0 scan | egrep "Cell|ESSID|Signal|Rates" | grep -A 2 -B 2 ' + DEFAULTSSIDNAMN).read())
    splittedList = output.split("\n")
    #prints.conditionalPrint(prints.wifiPrint, splittedList)

    newList = []
    for i in range(len(splittedList)):
        newList.append(stringFormatting.removeSpacesBeforeAndAfterString(splittedList[i]))
    #prints.conditionalPrint(prints.wifiPrint, newList)
    return newList

def filterByQuality(lst, threshold):
    global selectedNetwork
    global selectedNetworkQuality
    nw = {}

    for s in range(len(lst)):
        if "Cell" in lst[s]:
            try:
                nw[lst[s + 2]] = lst[s + 1]
            except Exception as e:
                print(e)

    #prints.conditionalPrint(prints.wifiPrint, nw)
    
    fnw = {}
    for k in nw.keys():
        key = k.split('"')[1]
        value = nw.get(k).split(" Signal")[0].split("=")[1].split(" ")[0].split("/")[0]
        fnw[key] = value

    networks = []
    bestNetwork = None

    os.system("clear")

    if prints.wifiPrint:
        print("\n<==============================Networks==============================>\n")
        print("Amount of available networks: " + str(len(list(fnw.keys()))) + "\n")
        for k in fnw.keys():
            print("Network: %s Quality %s/70." % (str(k), str(fnw.get(k))))
        print("\n")

    for k in fnw.keys():
        try:
            quality = int(fnw.get(k))
            if bestNetwork == None:
                #print("networkwasnone", k)
                bestNetwork = k
            elif len(list(fnw.keys())) == 1:
                print("Only one available existing network.")
            elif quality > int(fnw.get(bestNetwork)) + threshold:
                bestNetwork = k
            networks.append(k)
        except:
            pass

    #print("Currently connected to: %s. Quality %s/70." % (str(bestNetwork), str(fnw.get(bestNetwork))))

    return networks, bestNetwork

def changeConnection(bestNetwork):
    global currentlySelectedNetwork
    networks = str(os.popen('sudo wpa_cli list_networks | grep "Beltevogn"').read()).split("\n")
    exit = False
    for n in range(len(networks)):
        if exit or currentlySelectedNetwork == bestNetwork:
            break
        line = networks[n].split("\\")
        for word in range(len(line)):
            if exit:
                break
            if bestNetwork in line[word]:
                os.system("wpa_cli select_network " + str(line[0]))
                currentlySelectedNetwork = bestNetwork
                print("Changing to network " + currentlySelectedNetwork + ".")

main(update = 5, threshold = 5)