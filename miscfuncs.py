# Misc. Functions
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
    