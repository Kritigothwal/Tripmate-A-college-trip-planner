"""
emergency_contacts.py

Just a small helpful feature - shows some general emergency contact
numbers that are useful while travelling in India, plus lets the
user save one personal emergency contact (like a parent/guardian)
for their own reference during the trip.
"""

GENERAL_HELPLINES = {
    "National Emergency Number": "112",
    "Police": "100",
    "Ambulance": "102",
    "Women Helpline": "1091",
    "Railway Enquiry": "139",
    "Tourist Helpline": "1363"
}


def show_emergency_contacts():
    print("\n----- EMERGENCY HELPLINE NUMBERS -----")
    for name, number in GENERAL_HELPLINES.items():
        print(f"  {name:<28}: {number}")

    add_personal = input("\nDo you want to note down a personal emergency contact too? (y/n): ").strip().lower()

    if add_personal == "y":
        name = input("Contact name (e.g. Dad, Mom, Roommate): ").strip()
        number = input("Contact number: ").strip()
        print(f"\nSaved for this session -> {name}: {number}")
        print("(Tip: also save this number directly in your phone before you leave!)")
