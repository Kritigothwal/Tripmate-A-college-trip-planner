"""
destinations_data.py

This file just stores the information about all the destinations
that TripMate knows about. I kept it as a simple dictionary of
dictionaries so it is easy to read and easy to add more places later.

cost_per_day is a rough number in rupees per person (just for
estimation, not 100% accurate).
"""

DESTINATIONS = {
    "manali": {
        "state": "Himachal Pradesh",
        "type": "hills",
        "cost_per_day": 1800,
        "best_time": "March to June, Dec to Jan (for snow)",
        "activities": ["Solang Valley", "Hidimba Temple", "Old Manali cafes", "River rafting"]
    },
    "goa": {
        "state": "Goa",
        "type": "beach",
        "cost_per_day": 2200,
        "best_time": "November to February",
        "activities": ["Beach hopping", "Water sports", "Fort Aguada", "Night markets"]
    },
    "jaipur": {
        "state": "Rajasthan",
        "type": "city",
        "cost_per_day": 1500,
        "best_time": "October to March",
        "activities": ["Amber Fort", "Hawa Mahal", "City Palace", "Local bazaars"]
    },
    "rishikesh": {
        "state": "Uttarakhand",
        "type": "religious/adventure",
        "cost_per_day": 1200,
        "best_time": "September to April",
        "activities": ["River rafting", "Laxman Jhula", "Ganga Aarti", "Camping"]
    },
    "varanasi": {
        "state": "Uttar Pradesh",
        "type": "religious",
        "cost_per_day": 1000,
        "best_time": "October to March",
        "activities": ["Ganga Aarti", "Boat ride", "Kashi Vishwanath Temple"]
    },
    "ooty": {
        "state": "Tamil Nadu",
        "type": "hills",
        "cost_per_day": 1600,
        "best_time": "April to June",
        "activities": ["Botanical Garden", "Ooty Lake", "Toy Train"]
    },
    "mumbai": {
        "state": "Maharashtra",
        "type": "city",
        "cost_per_day": 2500,
        "best_time": "November to February",
        "activities": ["Gateway of India", "Marine Drive", "Film city tour"]
    },
    "amritsar": {
        "state": "Punjab",
        "type": "religious",
        "cost_per_day": 1300,
        "best_time": "October to March",
        "activities": ["Golden Temple", "Wagah Border", "Jallianwala Bagh"]
    }
}


def get_destination_names():
    # returns a simple list of all destination names (as a list, not dict)
    names = []
    for place in DESTINATIONS:
        names.append(place)
    return names


def search_destination(name):
    """
    Looks up a destination by name (not case sensitive).
    Returns the info dictionary if found, otherwise None.
    """
    name = name.lower().strip()
    if name in DESTINATIONS:
        return DESTINATIONS[name]
    else:
        return None


def search_by_type(trip_type):
    """
    Returns a list of (name, info) for every destination matching
    the given type, e.g. 'beach', 'hills', 'religious', 'city'.
    """
    trip_type = trip_type.lower().strip()
    results = []
    for name, info in DESTINATIONS.items():
        if trip_type in info["type"]:
            results.append((name, info))
    return results
