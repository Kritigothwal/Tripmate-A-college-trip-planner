 Problem Statement - TripMate

## Problem Statement

College students often plan short trips with friends during breaks
or long weekends, but most of the time this planning happens in a
very unorganized way - a random WhatsApp chat, no clear budget, and
someone always forgets something important to pack. There is no
simple, free tool made specifically for a student's small trip that
handles the destination search, budget, itinerary and packing
together. TripMate tries to solve this by giving a single,
easy-to-use command line program that a student can run to plan
their trip from start to end.

## Scope of the Project

TripMate is built as a **console based (command line) Python
application** for individual use. It is meant to help with the
*planning* stage of a trip - it does not do real-time booking of
tickets/hotels, and it does not connect to the internet or any live
API. All destination data used for budget/itinerary suggestions is
stored locally inside the program (a small built-in database of
common Indian destinations). All trip records the student saves are
stored locally in a CSV file on their own computer.

This is an academic mini-project built to demonstrate the Python
concepts learned in the first year of Integrated Mtech AI - it is intentionally
kept simple and does not aim to be a production-level travel booking
platform.

## Target Users

- College / university students planning short trips or college
  trips with friends.
- Anyone who wants a very simple, offline way to rough out a travel
  budget and itinerary without using a paid app.

## High-Level Features

- Plan a new trip (starting point, destination, days, people, trip
  type)
- Search destinations by name or by type
- Calculate an estimated travel budget (transport + hotel + food +
  activities)
- Compare transport modes (Bus / Train / Flight / Cab)
- Generate a simple day-wise itinerary
- Show a packing checklist based on trip type
- Save trips to a file and view previously saved trips
- Show emergency helpline numbers useful while travelling
