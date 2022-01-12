import fileHandling as fh
#Gloym denne fila
pathToHere = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

#startupFile = "/etc/rc.local"
#command = "sh /home/pi/Tanks/start.sh &"
#contentFromFile = fh.readTXTFile(startupFile)
#contentFromFile = str(contentFromFile).split("\n")
#print(contentFromFile)

#fh.replaceLineInFile(startupFile, fh.getLineNumberFromFile(startupFile, "exit 0"))