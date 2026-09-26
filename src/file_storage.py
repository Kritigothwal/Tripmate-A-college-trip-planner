"""
file_storage.py

Takes care of saving and loading the trips the user has planned.
I am using a simple CSV (comma separated) text file for this since
we have covered basic file handling in class. No external database
is used - this file itself acts like a mini database table.

File used: data/saved_trips.csv
Format of each line:
start,destination,days,people,trip_type,total_budget
"""

import os
import csv

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "saved_trips.csv")


def save_trip(trip, total_budget=0):
    """
    Appends one trip to the CSV file. If the file/folder does not
    exist yet, it creates it first.
    """
    folder = os.path.dirname(DATA_FILE)
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_exists = os.path.exists(DATA_FILE)

    try:
        with open(DATA_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                # write header only once, when file is created for the first time
                writer.writerow(["start", "destination", "days", "people", "trip_type", "total_budget"])
            writer.writerow([
                trip["start"],
                trip["destination"],
                trip["days"],
                trip["people"],
                trip["trip_type"],
                total_budget
            ])
        print("\nTrip saved successfully!")
    except Exception as e:
        # basic error handling as mentioned in project guidelines
        print("Something went wrong while saving the trip:", e)


def load_all_trips():
    """
    Reads all saved trips from the CSV file and returns them as a
    list of dictionaries. Returns an empty list if no file exists.
    """
    trips = []

    if not os.path.exists(DATA_FILE):
        return trips

    try:
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                trips.append(row)
    except Exception as e:
        print("Could not read saved trips:", e)

    return trips


def view_saved_trips():
    trips = load_all_trips()

    if len(trips) == 0:
        print("\nNo trips have been saved yet.")
        return

    print("\n----- YOUR SAVED TRIPS -----")
    for index, trip in enumerate(trips, start=1):
        print(f"\nTrip {index}:")
        print(f"  From        : {trip['start']}")
        print(f"  Destination : {trip['destination']}")
        print(f"  Days        : {trip['days']}")
        print(f"  People      : {trip['people']}")
        print(f"  Type        : {trip['trip_type']}")
        print(f"  Budget      : Rs. {trip['total_budget']}")
