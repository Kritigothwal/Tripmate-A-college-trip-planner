"""
budget_calculator.py

This module calculates a rough total budget for the trip based on
transport, hotel, food and activities. The numbers are just
estimates (per day / per person), this is not meant to be 100%
accurate, just enough to give the student an idea while planning.
"""

# these are rough default rates, can be changed depending on trip type
HOTEL_RATE_PER_DAY = 1000       # per room per day (assuming 2 people share)
FOOD_RATE_PER_DAY = 500         # per person per day
ACTIVITY_RATE_PER_DAY = 400     # per person per day

TRANSPORT_BASE_COST = {
    "bus": 800,
    "train": 1200,
    "flight": 4500,
    "cab": 2500
}


def calculate_budget(trip):
    days = trip["days"]
    people = trip["people"]

    print("\nHow are you planning to travel?")
    print("1. Bus")
    print("2. Train")
    print("3. Flight")
    print("4. Cab")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        transport_mode = "bus"
    elif choice == "2":
        transport_mode = "train"
    elif choice == "3":
        transport_mode = "flight"
    elif choice == "4":
        transport_mode = "cab"
    else:
        print("Invalid choice, taking bus as default.")
        transport_mode = "bus"

    transport_cost = TRANSPORT_BASE_COST[transport_mode] * people

    # rooms needed, assuming 2 people can share one room
    rooms_needed = (people + 1) // 2
    hotel_cost = HOTEL_RATE_PER_DAY * rooms_needed * days

    food_cost = FOOD_RATE_PER_DAY * people * days
    activity_cost = ACTIVITY_RATE_PER_DAY * people * days

    total = transport_cost + hotel_cost + food_cost + activity_cost

    print("\n----- ESTIMATED BUDGET -----")
    print(f"Transport ({transport_mode})   : Rs. {transport_cost}")
    print(f"Hotel ({rooms_needed} room/s)      : Rs. {hotel_cost}")
    print(f"Food                    : Rs. {food_cost}")
    print(f"Activities              : Rs. {activity_cost}")
    print("-" * 30)
    print(f"TOTAL ESTIMATED BUDGET  : Rs. {total}")
    print("-" * 30)

    budget_breakdown = {
        "transport": transport_cost,
        "hotel": hotel_cost,
        "food": food_cost,
        "activities": activity_cost,
        "total": total,
        "transport_mode": transport_mode
    }

    return budget_breakdown
