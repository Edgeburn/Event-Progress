import datetime as dt
from CalEvent import *
from miscfuncs import *

# Read date from YYYY/MM/DD format
# Year = 0:4
# Month = 5:7
# Day = 8:10

clearTerminal()

events = []  # Main events list

# Read all files in current directory for processing
eventFileNames = []

with os.scandir() as filesInDirectory:  # Get all files in directory, and load their filenames into a list
    for file in filesInDirectory:
        eventFileNames.append(file.name)

eventFileNames = list(filter(isEbmevtFile, eventFileNames))  # Ignore files which aren't EventProgress files


appIsRunning = False

while appIsRunning:
    pass
