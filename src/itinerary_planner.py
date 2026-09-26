"""
itinerary_planner.py

Generates a simple day-wise itinerary (schedule) for the trip.
It uses the activities list from destinations_data.py if the
destination is found in our database, otherwise it just gives a
generic plan.
"""

from destinations_data import search_destination

# a generic time-slot template used for every day
TIME_SLOTS = ["09:00 AM", "11:00 AM", "02:00 PM", "04:00 PM", "08:00 PM"]

GENERIC_PLAN = [
    "Check-in / Breakfast",
    "Visit main attraction",
    "Lunch break",
    "Local sightseeing / shopping",
    "Return to hotel / dinner"
]


def generate_itinerary(trip):
    print(f"\n----- ITINERARY FOR {trip['destination'].upper()} -----")

    dest_info = search_destination(trip["destination"])
    activities = []

    if dest_info is not None:
        activities = dest_info["activities"]

    for day in range(1, trip["days"] + 1):
        print(f"\nDay {day}:")
        for i in range(len(TIME_SLOTS)):
            if activities and i < len(activities):
                # mix a real activity from the database into the plan
                plan_item = activities[i % len(activities)]
            else:
                plan_item = GENERIC_PLAN[i % len(GENERIC_PLAN)]
            print(f"  {TIME_SLOTS[i]} -> {plan_item}")

    print("\n(This is a suggested plan, feel free to adjust timings)")
