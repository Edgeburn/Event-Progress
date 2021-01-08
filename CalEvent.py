import datetime as dt

class CalEvent:
    """
    Class representing a calendar event
    """

    def __init__(self, filename) -> None:
        try:
            fileToParse = open(f"{filename}.ebmevt")
        except FileNotFoundError:
            print(f"Tried to open \"{filename}.ebmevt\", but it doesn't exist.")
            del self
        fileContents = fileToParse.readlines()  # Load each line of the file into a list

        assert fileContents[0] == "FILEVERSION=V1"  # Ensure that the version of the file is correct

        unparsedTitle = fileContents[1]
        unparsedDescription = fileContents[2]
        unparsedStart = fileContents[3]
        unparsedEnd = fileContents[4]

        




    def getPercentage(self) -> int:
        """
        Returns the percentage of the time elapsed between two dates. Uses the current date as default for the elapsed progress, can be specified.
        """

        # Check that all arguments are of the correct type.
        if not isinstance(start, dt.date):
            raise TypeError("start time is not of object type date")
        elif not isinstance(end, dt.date):
            raise TypeError("End time is not of object type date")
        elif not isinstance(current, dt.date):
            raise TypeError("Current time is not of object type date")

        if start == end:
            raise RuntimeError("start and end of event are equal!")

        unixTime1970 = dt.date(1970, 1, 1)  # The start of UNIX time as a variable for simplicity.

        # Convert dates to UNIX timestamps as ints
        startUnixTimestamp = (start - unixTime1970) / dt.timedelta(seconds=1)
        endUnixTimestamp = (end - unixTime1970) / dt.timedelta(seconds=1)
        currentUnixTimestamp = (current - unixTime1970) / dt.timedelta(seconds=1)

        return round((currentUnixTimestamp - startUnixTimestamp) / (endUnixTimestamp - startUnixTimestamp) * 100)



