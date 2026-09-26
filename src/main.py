"""
main.py

TripMate - A Student Friendly College Travel Planner
------------------------------------------------------
This is the main file that runs the whole program. It just shows a
menu in a loop and calls the correct function from the other files
depending on what the user chooses.

How to run:
    python main.py

Author: Kriti Gothwal
"""

from trip_planner import create_new_trip, show_trip_summary
from budget_calculator import calculate_budget
from transport_compare import compare_transport
from itinerary_planner import generate_itinerary
from packing_checklist import show_packing_list
from destinations_data import get_destination_names, search_destination, search_by_type
from file_storage import save_trip, view_saved_trips
from emergency_contacts import show_emergency_contacts


def print_menu():
    print("\n")
    print("=" * 40)
    print("      TRIPMATE - COLLEGE TRAVEL PLANNER")
    print("=" * 40)
    print("1. Plan a New Trip")
    print("2. Search Destinations")
    print("3. Calculate Travel Budget")
    print("4. Plan Daily Itinerary")
    print("5. Packing Checklist")
    print("6. Compare Transport Options")
    print("7. Save Current Trip")
    print("8. View Saved Trips")
    print("9. Emergency Contacts")
    print("10. Exit")
    print("=" * 40)


def search_destinations_menu():
    print("\n----- SEARCH DESTINATIONS -----")
    print("1. Search by name")
    print("2. Search by trip type (beach/hills/city/religious)")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter destination name: ").strip()
        info = search_destination(name)
        if info is None:
            print("Sorry, this destination is not in our database.")
            print("Available destinations:", ", ".join(get_destination_names()))
        else:
            print(f"\n{name.title()} ({info['state']})")
            print(f"Type          : {info['type']}")
            print(f"Best time     : {info['best_time']}")
            print(f"Approx cost/day: Rs. {info['cost_per_day']}")
            print("Popular activities:")
            for activity in info["activities"]:
                print(f"  - {activity}")

    elif choice == "2":
        trip_type = input("Enter type (beach/hills/city/religious): ").strip()
        results = search_by_type(trip_type)
        if len(results) == 0:
            print("No destinations found for this type.")
        else:
            print(f"\nDestinations matching '{trip_type}':")
            for name, info in results:
                print(f"  - {name.title()} ({info['state']})")
    else:
        print("Invalid choice.")


def main():
    current_trip = None          # keeps the trip that is currently being planned
    current_budget = 0           # budget calculated for the current trip

    print("Welcome to TripMate!")
    print("Plan your next college trip easily :)")

    while True:
        print_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            current_trip = create_new_trip()
            current_budget = 0  # reset budget since it's a new trip

        elif choice == "2":
            search_destinations_menu()

        elif choice == "3":
            if current_trip is None:
                print("\nPlease plan a trip first (option 1).")
            else:
                budget_details = calculate_budget(current_trip)
                current_budget = budget_details["total"]

        elif choice == "4":
            if current_trip is None:
                print("\nPlease plan a trip first (option 1).")
            else:
                generate_itinerary(current_trip)

        elif choice == "5":
            if current_trip is None:
                trip_type = input("Enter trip type (college/trek/beach/city/religious): ").strip()
                show_packing_list(trip_type)
            else:
                show_packing_list(current_trip["trip_type"])

        elif choice == "6":
            compare_transport()

        elif choice == "7":
            if current_trip is None:
                print("\nPlease plan a trip first (option 1).")
            else:
                save_trip(current_trip, current_budget)

        elif choice == "8":
            view_saved_trips()

        elif choice == "9":
            show_emergency_contacts()

        elif choice == "10":
            print("\nThanks for using TripMate. Have a safe trip! :)")
            break

        else:
            print("\nInvalid choice, please enter a number between 1 and 10.")


# this makes sure main() only runs when this file is run directly
if __name__ == "__main__":
    main()
