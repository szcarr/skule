#Merkesdal

import os

def getMyGlobalIp():
    globalIP = os.popen("dig +short myip.opendns.com @resolver1.opendns.com").read()
    splitList = globalIP.split("\n")
    failedText = "No global IP."
    result = failedText
    try:
        if splitList:
            result = splitList[0]
        if "failure" in result:
            result = failedText
        elif splitList[0] == "":
            result = failedText
    except:
        print("Failed to get global IP address.")
        result = failedText
    return result

def getMyLocalIp():
    #Dynamically returns my IP
    output = os.popen("ip a | grep 'inet ...' | awk -F' ' '{print $2'}").read()
    ipSingleString = ""
    ipList = []
    for c in output: #Makes it to a single string
        if c == "\n":
            ipList.append(ipSingleString)
            ipSingleString = ""
            continue
        ipSingleString = ipSingleString + c
    result = "No local IP."
    try:
        if ipList:
            result = ipList[1]
    except:
        print("Failed to get local IP address.")
        result = "No local IP."
    return result