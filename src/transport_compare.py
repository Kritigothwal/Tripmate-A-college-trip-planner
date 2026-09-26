"""
transport_compare.py

Shows a simple comparison table between Bus, Train, Flight and Cab
so the user can decide what suits them best in terms of cost, time
and comfort. All values here are just rough estimates for a
medium-distance trip (around 400-500 km), since we don't have a
real-time travel API for this project.
"""

TRANSPORT_OPTIONS = [
    {"mode": "Bus",    "cost_per_person": 800,  "time_hours": 10, "comfort": "Medium"},
    {"mode": "Train",  "cost_per_person": 1200, "time_hours": 8,  "comfort": "Medium-High"},
    {"mode": "Flight", "cost_per_person": 4500, "time_hours": 2,  "comfort": "High"},
    {"mode": "Cab",    "cost_per_person": 2500, "time_hours": 7,  "comfort": "High"},
]


def compare_transport():
    print("\n----- TRANSPORT COMPARISON (approx, for ~450 km) -----")
    print(f"{'Mode':<10}{'Cost/Person':<15}{'Time (hrs)':<15}{'Comfort':<12}")
    print("-" * 52)

    for option in TRANSPORT_OPTIONS:
        print(f"{option['mode']:<10}{'Rs. ' + str(option['cost_per_person']):<15}"
              f"{option['time_hours']:<15}{option['comfort']:<12}")

    print("-" * 52)
    print("Tip: Flight is fastest but costliest. Bus is cheapest but takes longer.")

    # let the user pick the cheapest / fastest automatically, just for fun
    cheapest = min(TRANSPORT_OPTIONS, key=lambda x: x["cost_per_person"])
    fastest = min(TRANSPORT_OPTIONS, key=lambda x: x["time_hours"])

    print(f"\nCheapest option : {cheapest['mode']} (Rs. {cheapest['cost_per_person']})")
    print(f"Fastest option  : {fastest['mode']} ({fastest['time_hours']} hrs)")
