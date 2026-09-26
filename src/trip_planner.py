"""
trip_planner.py

Handles taking the basic trip details from the user - starting
place, destination, number of days and number of people.

I am storing a trip as a simple dictionary because we have not been
taught proper classes/objects in detail, dictionaries do the job
fine for this project.
"""

from destinations_data import search_destination


def create_new_trip():
    print("\n----- PLAN A NEW TRIP -----")

    start = input("Enter your starting location: ").strip().title()
    destination = input("Enter destination (e.g. Manali, Goa, Jaipur): ").strip()

    dest_info = search_destination(destination)
    if dest_info is None:
        print("Note: this destination is not in our database yet,")
        print("so budget suggestions might not be very accurate.")

    # basic input validation using a loop, keep asking till valid number
    while True:
        days_input = input("Number of days for the trip: ").strip()
        if days_input.isdigit() and int(days_input) > 0:
            days = int(days_input)
            break
        else:
            print("Please enter a valid positive number of days.")

    while True:
        people_input = input("Number of people travelling: ").strip()
        if people_input.isdigit() and int(people_input) > 0:
            people = int(people_input)
            break
        else:
            print("Please enter a valid positive number of people.")

    trip_type = input("What kind of trip is this? (college/trek/beach/city/religious): ").strip().lower()

    trip = {
        "start": start,
        "destination": destination.title(),
        "days": days,
        "people": people,
        "trip_type": trip_type
    }

    print("\nGreat! Here is a summary of your trip:")
    show_trip_summary(trip)

    return trip


def show_trip_summary(trip):
    print("-" * 35)
    print(f"From         : {trip['start']}")
    print(f"Destination  : {trip['destination']}")
    print(f"Days         : {trip['days']}")
    print(f"People       : {trip['people']}")
    print(f"Trip type    : {trip['trip_type']}")
    print("-" * 35)
