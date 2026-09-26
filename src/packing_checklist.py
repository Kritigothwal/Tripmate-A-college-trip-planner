"""
packing_checklist.py

Gives a packing checklist based on the type of trip the student
selects. Kept as simple lists inside a dictionary - easy to update.
"""

COMMON_ITEMS = ["ID card / College ID", "Phone charger", "Power bank", "Water bottle", "Basic first aid kit"]

CHECKLISTS = {
    "college": ["Comfortable clothes", "Extra pair of shoes", "Notebook (if any group activity)", "Camera/phone for photos"],
    "trek": ["Trekking shoes", "Rain jacket", "Torch/flashlight", "Energy bars", "Extra socks", "Cap/hat"],
    "beach": ["Swimwear", "Sunscreen", "Sunglasses", "Flip-flops", "Beach towel"],
    "city": ["Comfortable walking shoes", "Light jacket", "Map/offline maps downloaded"],
    "religious": ["Modest clothing", "Small cash pouch (for donations)", "Comfortable footwear (easy to remove)"]
}


def show_packing_list(trip_type):
    trip_type = trip_type.lower().strip()

    print(f"\n----- PACKING CHECKLIST ({trip_type.title()} Trip) -----")

    print("Common items for every trip:")
    for item in COMMON_ITEMS:
        print(f"  [ ] {item}")

    if trip_type in CHECKLISTS:
        print(f"\nSpecific items for a {trip_type} trip:")
        for item in CHECKLISTS[trip_type]:
            print(f"  [ ] {item}")
    else:
        print("\nNo specific list found for this trip type, but the common list above should help.")
