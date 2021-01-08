import datetime as dt

def getPercentage(beginning, end, current = dt.date.today()) -> int:
    """
    Returns the percentage of the time elapsed between two dates. Uses the current date as default for the elapsed progress, can be specified.
    """

    # Check that all arguments are of the correct type.
    if not isinstance(beginning, dt.date):
        raise TypeError("Beginning time is not of object type date")
    elif not isinstance(end, dt.date):
        raise TypeError("End time is not of object type date")
    elif not isinstance(current, dt.date):
        raise TypeError("Current time is not of object type date")

    if beginning == end:
        raise RuntimeError("Beginning and end of event are equal!")

    unixTime1970 = dt.date(1970, 1, 1)  # The beginning of UNIX time as a variable for simplicity.

    # Convert dates to UNIX timestamps as ints
    beginningUnixTimestamp = (beginning - unixTime1970) / dt.timedelta(seconds=1)
    endUnixTimestamp = (end - unixTime1970) / dt.timedelta(seconds=1)
    currentUnixTimestamp = (current - unixTime1970) / dt.timedelta(seconds=1)

    return round((currentUnixTimestamp - beginningUnixTimestamp) / (endUnixTimestamp - beginningUnixTimestamp) * 100)


print("Input dates in YYYY/MM/DD format")
beginningDateRaw = input("Beginning date > ")
endDateRaw = input("End date > ")

beginningYear = int(beginningDateRaw[0:4])
beginningMonth = int(beginningDateRaw[5:7])
beginningDay = int(beginningDateRaw[8:10])

endYear = int(endDateRaw[0:4])
endMonth = int(endDateRaw[5:7])
endDay = int(endDateRaw[8:10])


beginning = dt.date(beginningYear, beginningMonth, beginningDay)
end = dt.date(endYear, endMonth, endDay)
percentageCompleted = getPercentage(beginning, end)
print(f"As of today, it is {percentageCompleted}% between {beginning} and {end}.")
