from typing import get_origin
import globals
import datetime as dt
import os
from miscfuncs import *

class CalEvent:
	"""
	Class representing a calendar event
	"""

	start = 0
	end = 0
	title = 0
	description = 0
	id = -1
	filename = 0


	def __init__(self, filename, id) -> None:
		try:
			try:
				fileToParse = open(f"{filename}")
			except FileNotFoundError:
				raise FileNotFoundError(f"Tried to open \"{filename}.ebmevt\", but it doesn't exist.")
			fileContents = fileToParse.readlines()  # Load each line of the file into a list

			for i in range(len(fileContents)):  # Remove all newline characters
				fileContents[i] = fileContents[i].replace("\n", "")

			assert len(fileContents) != 0, f"File {filename} is empty"
			assert fileContents[0] == "FILEVERSION=V1", f"File {filename} is of incorrect version"  # Ensure that the version of the file is correct

			fileToParse.close()
			self.filename = filename

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
		except:
			self.filename = filename
			self.id = id
			self.title = "Unreadable event file"
			self.description = "An error occurred when trying to read this event file."
			self.start = dt.date.today()
			self.end = dt.date.today()

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
			return 100

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

		if self.getPercentage() > 100:
			return "[####################]"
		elif self.getPercentage() < 0:
			return "[                    ]"
		else:
			numOfFilledUnits = int((self.getPercentage() / 100) * 20)
			numOfUnFilledUnits = 20 - numOfFilledUnits
			filledUnitsString = "#" * numOfFilledUnits
			unFilledUnitsString = " " * numOfUnFilledUnits
			return f"[{filledUnitsString}{unFilledUnitsString}]"
		


	def saveFile(self):
		"""
		Save the file with updated information to the disk
		"""
		fileToWrite = globals.events[self.id]
		fileToWrite = fileToWrite.filename
		fileToWrite = open(fileToWrite, "w")

		toWrite = []

		toWrite.append("FILEVERSION=V1\n")
		toWrite.append(f"TITLE={self.title}\n")
		toWrite.append(f"DESCRIPTION={self.description}\n")
		toWrite.append(f"START={self.start.year}-{fileSaveNumberParser(self.start.month)}-{fileSaveNumberParser(self.start.day)}\n")
		toWrite.append(f"END={self.end.year}-{fileSaveNumberParser(self.end.month)}-{fileSaveNumberParser(self.end.day)}\n")

		fileToWrite.writelines(toWrite)
		
		fileToWrite.close()
		reloadEvts()


	def fullOverview(self):
		"""
		Give a full overview of the given event
		"""
		clearTerminal()
		print("----------------------------------------------")
		print(f"Event #{self.id} ({self.filename})")
		print("")
		print(self.title)
		print(self.description)
		print("")
		print(f"{self.start} through {self.end}")
		print(f"{self.generateProgressBar()} {self.getPercentage()}% Complete")
		print("----------------------------------------------")
		print("\n\n")


	def editEvent(self):
		"""
		Activate a prompt wherein the details of the event can be changed, and then saves it to the disk.
		"""
		clearTerminal()
		print("Editing this event.")
		print(self)
		print("To leave a value unchanged, leave your response blank.")
		print("")

		# Collect new values from user
		newTitle = input(f"Title > ")
		newDescription = input(f"Description > ")
		newStart = input("Start date (YYYY-MM-DD) > ")
		newEnd = input("End date (YYYY-MM-DD) > ")

		# Check if values are empty; if they are, do not change values
		if newTitle != "":
			self.title = newTitle
		if newDescription != "":
			self.description = newDescription
		if newStart != "":
			self.start = processDate(newStart)
		if newEnd != "":
			self.end = processDate(newEnd)
		

		self.saveFile()

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



