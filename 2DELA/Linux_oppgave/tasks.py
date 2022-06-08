import Wifi.src.fileHandling as fh
import random
import stringGenerator
import os

projectFolder = "/home/scp092/Documents/Hacking/"
workingDirectory = fh.getPathToCurrentDir(projectFolder)
amountOfTasks = 4
splitBy = fh.detectOS()

verbose = True
cheater = True
cheaterPrint = True if verbose and cheater else False

def conditionalPrint(boolean, stringToPrint):
    if boolean:
        print(stringToPrint)

def removeTasks():
    for i in range(amountOfTasks):
        os.popen("rm -rf " + workingDirectory + "Task" + str(i + 1))

def task1():
    taskDir = workingDirectory + splitBy + "Task1"
    try:
        fh.makeDirectory(taskDir)
    except:
        conditionalPrint(verbose, "Folder already exists: " + taskDir)
        pass

    minimumAmountOfFiles = 30
    maximumAmountOfFiles = 60 - 1

    amountOfFiles = random.randrange(minimumAmountOfFiles, maximumAmountOfFiles)
    passwordFile = random.randrange(0, amountOfFiles)

    for i in range(amountOfFiles):
        fh.createFileInSpecifiedDir(taskDir + splitBy + "File" + str(i + 1))

    printedPassword = stringGenerator.generateRandomString(length = 64)
    password = printedPassword + "\n"
    fh.addTextToSpecifiedFile(taskDir + splitBy + "File" + str(passwordFile), password)

    conditionalPrint(cheaterPrint, "Password is: " + printedPassword)
    conditionalPrint(cheaterPrint, "File where password is located: File" + str(passwordFile))
    conditionalPrint(verbose, "Task 1 completed setting up.")

def task2():
    pass

def main():
    try:
        removeTasks()
    except Exception as e:
        conditionalPrint(verbose, e)
        pass
    task1()
    task2()

main()