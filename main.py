import globals
import datetime as dt
from CalEvent import *
from miscfuncs import *
globals.initialize()

# Read date from YYYY/MM/DD format
# Year = 0:4
# Month = 5:7
# Day = 8:10

clearTerminal()
reloadEvts()


appIsRunning = True

while appIsRunning:
    action = ""
    print(f"{len(globals.events)} events found. ")
    print("List all events with \"list\". To view more information about a particular event, enter the event’s ID. To edit, enter \"edit <event ID>\". To delete, enter \"delete <event ID>\". Enter \"new\" to create a new event. To quit, enter \"quit\".")
    action = input("> ")
    action = action.lower()

    if action == "quit":
        appIsRunning = False
    elif action == "reload":
        clearTerminal()
        print(f"Reloading {len(globals.events)} events...")
        reloadEvts()
        print(f"{len(globals.events)} events reloaded.")
        print("")
    elif action == "list":
        for i in range(len(globals.events)):
            print(globals.events[i])
    elif "delete" in action:
        clearTerminal()
        idOfEventToDelete = int(action[7:])
        filenameOfFileToDelete = globals.events[idOfEventToDelete].filename
        print("Delete the following event?")
        print(globals.events[idOfEventToDelete])
        deleteConfirmation = input("Confirm deletion [y/n] > ")
        deleteConfirmation = deleteConfirmation.lower()
        if deleteConfirmation == "y":
            if os.path.exists(filenameOfFileToDelete):
                try:
                    os.remove(filenameOfFileToDelete)
                except:
                    print("We couldn't delete the file due to an error")
            else:
                print(f"We couldn't delete \"{filenameOfFileToDelete}\" because it doesn't seem to exist.")
        else:
            clearTerminal()
        reloadEvts()
    elif "edit" in action:
        idOfEventToEdit = int(action[5:])
        globals.events[idOfEventToEdit].editEvent()
    elif action == "new":
        clearTerminal()
        print("--------------------")
        print("Create New Event")
        print("--------------------")
        print("\n")
        newEventFilename = input("File name for new event > ")
        if newEventFilename == "":
            newEventFilename = generateFilename()
        if doesFilenameExist(newEventFilename):
            newEventFilename = f"{newEventFilename} (1)"
        newEventFilename = f"{newEventFilename}.ebmevt"
        newEventFile = open(newEventFilename, "w")

        # Write data to file
        dataToWrite = []
        dataToWrite.append("FILEVERSION=V1\n")
        dataToWrite.append("TITLE=Untitled Event\n")
        dataToWrite.append("DESCRIPTION=\n")
        dataToWrite.append(f"START={dt.date.today()}\n")
        dataToWrite.append(f"END={dt.date.today()}\n")
        newEventFile.writelines(dataToWrite)
        newEventFile.close()
        reloadEvts()

        # Find the event ID of the event that was just created
        idOfNewEvent = -1
        for i in range(len(globals.events)):
            if globals.events[i].filename == newEventFilename:
                idOfNewEvent = i
                break

        globals.events[idOfNewEvent].editEvent()


    else:
        try:  # This try-except block's purpose is to open the overview of a particular event only if the input is a number and a valid event ID, without causing a crash in the event that it isn't
            action = int(action)
            globals.events[action].fullOverview()
        except:
            print(f"Unknown command \"{action}\".")
