# Tripmate-A-college-trip-planner

This is my mini project made for the Vityarthi Python Essential flipped
course evaluation. I am a 1st year Integrated Mtech in AI and I built this
using core Python concepts taught in class - variables, loops,
conditionals, functions, lists, dictionaries and file handling.

## Overview

A lot of college students (including me and my friends) plan short
trips but end up guessing the budget and forgetting things to pack.
TripMate is a simple menu-driven, command line Python program that
helps a student plan a trip from start to end - deciding the
destination, estimating the budget, comparing transport options,
generating a day-wise itinerary, and keeping a packing checklist,
all in one place.

## Features

1. **Plan a New Trip** - enter starting point, destination, number of
   days and number of people.
2. **Search Destinations** - search by name or by trip type
   (beach / hills / city / religious) from a small built-in
   destination database.
3. **Calculate Travel Budget** - estimates transport, hotel, food and
   activity cost based on user choices.
4. **Plan Daily Itinerary** - generates a simple day-by-day schedule
   using the destination's popular activities.
5. **Packing Checklist** - gives a checklist based on the type of
   trip (college / trek / beach / city / religious).
6. **Compare Transport Options** - shows cost, time and comfort for
   Bus, Train, Flight and Cab.
7. **Save Current Trip** - saves the trip and its budget to a CSV
   file (`data/saved_trips.csv`) using file handling.
8. **View Saved Trips** - reads back and shows all previously saved
   trips.
9. **Emergency Contacts** - shows general emergency helpline numbers
   for India and lets you note a personal contact for the trip.

## Technologies / Tools Used

- **Language:** Python 3
- **Concepts used:** functions, dictionaries, lists, loops,
  conditionals, string formatting, exception handling, file
  handling (CSV module)
- **Storage:** Plain CSV file (no external database used)
- **Version control:** Git & GitHub

## Project Structure

```
TripMate_Project/
│
├── src/
│   ├── main.py                 -> entry point, menu, connects everything
│   ├── trip_planner.py         -> takes trip details from user
│   ├── budget_calculator.py    -> calculates estimated budget
│   ├── transport_compare.py    -> compares bus/train/flight/cab
│   ├── itinerary_planner.py    -> builds day-wise itinerary
│   ├── packing_checklist.py    -> gives packing list by trip type
│   ├── destinations_data.py    -> built-in destination database
│   ├── file_storage.py         -> save/load trips using CSV file
│   └── emergency_contacts.py   -> shows helpline numbers
│
├── data/
│   └── saved_trips.csv         -> created automatically when a trip is saved
│
├── diagrams/                   -> design diagrams (architecture, UML, etc.)
│
├── README.md
├── statement.md
└── TripMate_Project_Report.pdf -> full project report
```

## Steps to Install & Run

1. Make sure Python 3.8 or above is installed on your system.
   Check with:
   ```
   python --version
   ```
2. Open a terminal inside the `src` folder.
3. Run the program:
   ```
   python main.py
   ```
4. Use the on-screen menu (enter a number from 1-10) to use the
   different features.

No extra libraries are required to run the project - it only uses
Python's built-in `os` and `csv` modules.

## Instructions for Testing

- Choose option **1** first to plan a trip (this needs to be done
  before options 3, 4 and 7 will work properly).
- Try option **2** and search for destinations like `manali`, `goa`,
  `jaipur`, `rishikesh`, `varanasi`, `ooty`, `mumbai`, `amritsar` -
  these are already in the database.
- Try entering an invalid choice (like `99`) to check that the
  program shows an error message instead of crashing.
- Try entering a negative number of days/people while planning a
  trip - the program will keep asking until a valid number is
  entered.
- Use option **7** to save a trip, then option **8** to confirm it
  was saved correctly by reading it back from the CSV file.

## Screenshots

(Screenshots of the running program can be added here after testing
on your own machine - see `TripMate_Project_Report.pdf` for a written
walkthrough of each feature.)

## Author

Made by: Kriti Gothwal 

Registration Number:26MIM10023

Submitted for: VITyarthi - Python Essentials Flipped Course
