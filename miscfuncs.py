# Misc. Functions
import globals
import datetime as dt
import os

def processDate(dateToProcess) -> dt.date:
    """
    Process a date in string format YYYY-MM-DD into a Date object
    """
    year = int(dateToProcess[0:4])
    month = int(dateToProcess[5:7])
    day = int(dateToProcess[8:10])
    return dt.date(year, month, day)

def clearTerminal():
    """
    Clears the terminal of previous outputs. 
    """
    from sys import platform
    if platform != "win32":
        print("\033[H\033[J")
    else:
        os.system("cls")

def isEbmevtFile(filename) -> bool:
    if ".ebmevt" in filename:
        return True
    else:
        return False

def reloadEvts():
    from CalEvent import CalEvent
    globals.events = []
        # Read all files in current directory for processing
    eventFileNames = []

    with os.scandir() as filesInDirectory:  # Get all files in directory, and load their filenames into a list
        for file in filesInDirectory:
            eventFileNames.append(file.name)

    eventFileNames = list(filter(isEbmevtFile, eventFileNames))  # Ignore files which aren't EventProgress files

    for i in range(len(eventFileNames)):  # Generate CalEvent objects for each file
        currentFilename = eventFileNames[i]
        globals.events.append(CalEvent(currentFilename, i))
    

def fileSaveNumberParser(num) -> str:
    if num < 10:
        return f"0{num}"
    else:
        return str(num)
