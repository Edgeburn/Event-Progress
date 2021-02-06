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


def doesFilenameExist(filenameToCheck) -> bool:
    for i in globals.events:
        if i.filename == filenameToCheck or i.filename == f"{filenameToCheck}.ebmevt":
            return True
    return False

def generateFilename() -> str:
    filenameFound = False
    potentialFilenameNumber = 1  # Get the first possible potential filename
    while not filenameFound:
        if doesFilenameExist(potentialFilenameNumber):
            potentialFilenameNumber += 1
        else:
            return potentialFilenameNumber

def eventSearch(searchTerm):
    """
    Finds events with the given search term in their title, description, or filename. Then prints out these events
    """
    searchTerm = searchTerm.lower()
    matchingEvents = []
    # Search for the search term in each thing
    for event in globals.events:
        if searchTerm in event.title.lower():
            matchingEvents.append(event)
        
        if searchTerm in event.description.lower():
            matchingEvents.append(event)

        if searchTerm in event.filename.lower():
            matchingEvents.append(event)

    clearTerminal()
    print(f"{len(matchingEvents)} results found for \"{searchTerm}\"")
    for event in matchingEvents:
        print(event)
