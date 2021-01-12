import datetime as dt

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
    print("\033[H\033[J")

class CalEvent:
    """
    Class representing a calendar event
    """

    start = 0
    end = 0
    title = 0
    description = 0
    id = -1


    def __init__(self, filename, id) -> None:
        try:
            fileToParse = open(f"{filename}.ebmevt")
        except FileNotFoundError:
            print(f"Tried to open \"{filename}.ebmevt\", but it doesn't exist.")
            del self
        fileContents = fileToParse.readlines()  # Load each line of the file into a list

        for i in range(len(fileContents)):  # Remove all newline characters
            fileContents[i] = fileContents[i].replace("\n", "")


        assert fileContents[0] == "FILEVERSION=V1"  # Ensure that the version of the file is correct

        unparsedTitle = fileContents[1]
        unparsedDescription = fileContents[2]
        unparsedStart = fileContents[3]
        unparsedEnd = fileContents[4]

        # Parse file
        self.title = unparsedTitle[6:]
        self.description = unparsedDescription[12:]
        self.start = unparsedStart[6:]
        self.end = unparsedEnd[4:]
        # Start and end still need further processing!

        self.start = processDate(self.start)
        self.end = processDate(self.end)
        
        self.id = id


    def getPercentage(self, current = dt.date.today()) -> int:
        """
        Returns the percentage of the time elapsed between two dates. Uses the current date as default for the elapsed progress, can be specified.
        """

        # Check that all arguments are of the correct type.
        if not isinstance(self.start, dt.date):
            raise TypeError("start time is not of object type date")
        elif not isinstance(self.end, dt.date):
            raise TypeError("End time is not of object type date")
        elif not isinstance(current, dt.date):
            raise TypeError("Current time is not of object type date")

        if self.start == self.end:
            raise RuntimeError("start and end of event are equal!")

        unixTime1970 = dt.date(1970, 1, 1)  # The start of UNIX time as a variable for simplicity.

        # Convert dates to UNIX timestamps as ints
        startUnixTimestamp = (self.start - unixTime1970) / dt.timedelta(seconds=1)
        endUnixTimestamp = (self.end - unixTime1970) / dt.timedelta(seconds=1)
        currentUnixTimestamp = (current - unixTime1970) / dt.timedelta(seconds=1)

        return round((currentUnixTimestamp - startUnixTimestamp) / (endUnixTimestamp - startUnixTimestamp) * 100)


    def generateProgressBar(self):
        """
        Generate a progress bar for event overviews with this format:

        [####################]
        """

        numOfFilledUnits = int((self.getPercentage() / 100) * 20)
        numOfUnFilledUnits = 20 - numOfFilledUnits
        filledUnitsString = "#" * numOfFilledUnits
        unFilledUnitsString = " " * numOfUnFilledUnits
        return f"[{filledUnitsString}{unFilledUnitsString}]"
        


    def saveFile(self):
        """
        Save the file with updated information to the disk
        """
        # TODO: Implement save file method
        raise NotImplementedError

    def __repr__(self) -> str:
        
        # Using __repr__ in order to simplify the small overview on program startup.

        progressBar = self.generateProgressBar()
        return f"""
---------------------------
{self.title} (#{self.id})
{self.description}
{progressBar} {self.getPercentage()}%
---------------------------
        """



