# EventProgress

*EventProgress* is a small Python program allowing you to see the progress through an event. This is a project for my ICS4U computer science course.

## I still don't get what this does?

Basically the percentage through 2 dates. If you are in a 30 day month, the 15th would be 50%. The 19th would be 63%.

Here's some examples of events you could create:

- A school semester
- An extended break from work or school
- Time from birth to significant life events

## Installation

EventProgress should be installed in its own folder due to the files it generates and reads. If using the Python script directly, keep all the files together.

### Windows Executable

You can download the latest stable release from the releases section of this repository. The executable is standalone. The executable may be incorrectly recognized as malware. If it is, you can add an antivirus exception to the folder in which EventProgress is installed. If you're uncomfortable with the executable due to this, you can instead download and run the Python script directly.

### Python Script (Windows, Mac, Linux)

1. `cd` to the folder in which you want to install EventProgress.
2. Clone the repository with `git clone https://github.com/Edgeburn/Event-Progress.git`.

## Usage

`cd` to the directory in which the program is installed, and then run `python main.py`.

You will be presented with a prompt that looks like this:

```
0 events found. 
List all events with "list". To view more information about a particular event, enter the event’s ID. To edit, enter "edit <event ID>". To delete, enter "delete <event ID>". Enter "new" to create a new event. To quit, enter "quit".
> 
```

If this is the first time you've run the program, there will be no events created. Enter the `new` to start the event creator, and follow the prompts. The filename and title are different values: the filename is what appears in the file system, and if left blank will default to the number of events found currently + 1. The title is what is shown in the event info.

If there are events created, enter `list` at the prompt to see a list of all of the events that the program found. Each event will appear in a format like this:

```
---------------------------
Event title (#0)
Event description
[####################] 100%
---------------------------
```

The number in brackets next to the event title is the event's ID. The event ID is not static; it is determined at each refresh of the events in the folder through the order the files are read. You can use the event ID to do a few tasks with the events. **When entering the event ID, do not include the #**. You can view a more detailed overview of the event which includes the start and end dates and the event's filename, by entering the event ID on its own at the prompt. So for event 0, you would just enter `0`. Event 0 could be deleted with `delete 0`, and could be edited with `edit 0`.

**IMPORTANT** When entering dates, make sure you follow the format *exactly*, so if you want 01 January 2021, enter `2021-01-01`, and not `2021-1-1`.

## Possible future features

These may or may not be added at some point. I may also just decide to abandon the project in it's current state.

- [ ] GUI
- [ ] Add support for times in addition to dates
- [ ] Allow for files formatted incorrectly to be skipped and ignored
- [x] When a new event is created with a blank event filename, check that the generated filename does not already exist
- [ ] Accept dates written in an incorrect format
- [ ] Search function

## Possible problems and their solutions

If you are having a problem, please check here for the solution before opening an issue.

### Problem

I get an error that looks something like this:

```
  File "main.py", line 20
    print(f"{len(globals.events)} events found. ")
                                                ^
SyntaxError: invalid syntax
```

### Possible Cause & Solution

You likely tried to run the program in Python 2 instead of Python 3. Try running the program with `python3 main.py` rather than `python main.py`. If this still doesn't work, make sure that you are using the latest version of Python.

---

### Problem

Crash or other error message upon opening the program or creating a new event.

### Possible Cause & Solution

The permissions for the folder are incorrect. Make sure that you have read-write access to the folder in which the program is installed.
