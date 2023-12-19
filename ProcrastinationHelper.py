import os
from datetime import datetime

# each event is stored as a tuple (start time, duration, description)
# each task is stored as a tuple (due date, time needed to complete, description)
# times stored as month/day hour:min
events = []
tasks = []

help_menu = """
Help Menu
--------------------
- add event: add an event to the calendar
- add task: add a task to the calendar
- remove event: remove a task from the calendar
- remove task: remove an event from the calendar
- display task: shows task list
- display events: shows upcoming events
- help: displays the help menu
- clear: clear the screen
- exit: exits the program
"""


def add_event(event_list):
  print("Make sure to pad single digit numebrs with 0, for example 09/03/2020 04:03")
  print("time format month/day/year hour:minute")
  event_list.append((input("start time: "), input("duration: "), input("description:")))
  try:
    return sorted(event_list,key=lambda event: datetime.strptime(event[0], "%m/%d/%Y %H:%M"))
  except ValueError:
    print("Time formatted wrong")


def add_task(task_list):
  print("Make sure to pad single digit numebrs with 0, for example 09/03/2020 04:03")
  print("time format month/day/year hour:minute")
  task_list.append((input("due date: "), input("time needed to finish: "),input("description: ")))
  try:
    return sorted(task_list, key=lambda event: datetime.strptime(event[0], "%m/%d/%Y %H:%M"))
  except ValueError:
    print("Time formatted wrong")


def remove_item(events_list):
  if events_list:
    description = input("exact description of event to remove: ")
    for event in events_list:
      if event[2] == description:
        events_list.remove(event)
        print("Event removed")
        return events_list
    print("Event not found")
  else:
    print("Nothing scheduled")
    return events_list


def display_events(events_list):
  if events_list:
    for event in events_list:
      print(event[2] + " starts at: " + event[0] + ", and last for " +
            event[1])
  else:
    print("Nothing scheduled")


def display_task(tasks_list):
  if tasks_list:
    for task in tasks_list:
      print(task[2] + " due at: " + task[0] + ", and last for " + task[1])
  else:
    print("Nothing scheduled")


print("Type help for list of commands")
while True:
  command = input("command: ").lower()

  if command == "add event":
    events = add_event(events)
  elif command == "remove event":
    events = remove_item(events
  elif command == "add task":
    task = add_task(tasks)
  elif command == "remove task":
    task = remove_item(tasks)
  elif command == "display events":
    display_events(events)
  elif command == "display task":
    display_task(tasks)
  elif command == "help":
    print(help_menu)
  elif command == "exit":
    break
  elif command == "clear":
    os.system("clear")
  else:
    print("command not found")
