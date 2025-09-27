# Create a simple timesheet app that records when you type a person’s
# name and uses the current time to clock them in or out.
# this is called: attendance (timesheet tracker)
# steps:
# user enters a person's name
# the app check wheather that person is clocked in
# (if not -> it records the current time as clock in )
# if yes -> it records the current time as clock out(and calculate how long they worked)
# Data stored in file or database
#
# Algorithm:
# initialize stoage(file or csv)
# wait for input (a person's name)
# if person is clocked in:
# if the person not in the active list -> record current timestamp as clock in
# if they are in the active list (record current timestamp as clock out+calc duration and store it)
# Save the record to the file
# repeat untill program stop
# tools:
# datetime,input
# storage :  Csv file
# Data structure : dict
import datetime
import csv
import os

FILENAME = "RecordNames.csv"

try:
    while True:
        print("Enter your Name:")
        name = input("> ").strip()
        now = datetime.datetime.now()
        today = now.date()

        # Create file if it doesn't exist
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Name", "Clock In", "Clock Out"])  # header

        # Read all existing rows
        with open(FILENAME, "r", newline="") as f:
            reader = list(csv.reader(f))

        # Check if user already clocked in today
        found = False
        for row in reader:
            if row and row[0] == str(today) and row[1] == name:
                found = True
                if row[3] == "":  # if clock-out is empty
                    row[3] = str(now.time())
                    print(f"Clock-out recorded for {name} at {now.time()}")
                else:
                    print(f"{name} already clocked in and out today.")
                break

        # If not found, add new clock-in
        if not found:
            reader.append([str(today), name, str(now.time()), ""])
            print(f"Clock-in recorded for {name} at {now.time()}")

        # Write everything back
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(reader)

        print(f"Finish entering data for: {name}")
        print("To quit press Ctrl+C")

except KeyboardInterrupt:
    print("\nProgram stopped!!!")
