from datetime import datetime
import random

class mode:
    choice = {1: "Flight", 2: "Cruise", 3: "Railway", 4: "Bus", 5: "Car"}
    sub_choice = {1: "Luxury/Business Class", 2: "Economy Class", 3: "AC Sleeper", 4: "Non-AC Sleeper", 5: "Chair car"}

passenger_list = []

print("Welcome to TWARC\n\t\t We help you Complete/Add Destinations to your Bucket list...")

while True:
    start = input("Enter your current city name: ").strip().capitalize()
    try:
        end = input("Enter your destination: ").strip().capitalize()
        break
    except ValueError:
        print("Enter a valid destination")

while True:
    try:
        d = input("Date of your trip in DD/MM/YYYY: ").strip()
        t_d = datetime.strptime(d, "%d/%m/%Y")
        
        if t_d.date() < datetime.now().date():
            print("Enter a valid future Date.")
            continue
        break
    except ValueError:
        print("Invalid format. Please use DD/MM/YYYY.")

# --- TRANSPORTATION SELECTION ---
while True:
    try:
        print("\nSelect your mode of transport:")
        for key, value in mode.choice.items():
            print(f"{key}: {value}")
        
        c = int(input("Enter number between 1-5: "))
        if c in mode.choice:
            break
        print("Enter valid choice")
    except ValueError:
        print("Enter valid choice number")

# --- CLASS SELECTION ---
while True:
    try:
        print(f"\nSelect your class for {mode.choice[c]}:")
        for key, value in mode.sub_choice.items():
            print(f"{key}. {value}")
            
        sc = int(input("Enter number between 1-5: "))
        if sc in mode.sub_choice:
            chosen_class = mode.sub_choice[sc]
            break
        print("Enter a valid choice.")
    except ValueError:
        print("Enter a valid choice number.")

# --- PASSENGER COUNT ---
while True:
    try:
        num_passengers = int(input("\nEnter the number of passengers: "))
        if num_passengers > 0:
            break
        print("Please enter at least 1 passenger.")
    except ValueError:
        print("Invalid number. Please enter an integer.")

# --- COLLECT PASSENGER DETAILS ---
for i in range(num_passengers):
    print(f"\n--- Passenger {i + 1} Details ---")
    while True:
        name = input("Enter full name: ").strip().title()
        if name:
            break
        print("Name cannot be empty.")
        
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 120:
                break
            print("Please enter a realistic age (0-120).")
        except ValueError:
            print("Invalid age. Please enter a number.")

    while True:
        gov_id = input("Enter Government ID: ").strip()
        if gov_id:
            break
        print("Government ID cannot be empty.")

    # Added to the safely named passenger_list
    passenger_list.append({
        "name": name,
        "age": age,
        "Govt.ID": gov_id,
    })

# DISPLAY FINAL TICKET SUMMARY 
text=f"""
==========================================
            TWARC BOOKING SUMMARY            
==========================================
Route:       {start} ➔ {end}
Date:        {d}
Transport:   {mode.choice[c]} ({chosen_class})
Booking ID:  {random.randint(100, 1000)}
Total passengers: {num_passengers}
"""

# Calculate Fare
if c == 1:
    if chosen_class == "Luxury/Business Class":
        fare = num_passengers * 300000
    else:
        fare = num_passengers * 150000
elif c == 2:
    fare = num_passengers * 100000
elif c == 3:
    if chosen_class == "Luxury/Business Class":
        fare = num_passengers * 30000
    elif chosen_class == "Economy Class":
        fare = num_passengers * 15000
    elif chosen_class == "AC Sleeper":
        fare = num_passengers * 10000
    elif chosen_class == "Non-AC Sleeper":
        fare = num_passengers * 950
    else:
        fare = num_passengers * 500
elif c == 4:
    if chosen_class == "Luxury/Business Class":
        fare = num_passengers * 3000
    elif chosen_class == "Economy Class":
        fare = num_passengers * 1500
    elif chosen_class == "AC Sleeper":
        fare = num_passengers * 1000
    elif chosen_class == "Non-AC Sleeper":
        fare = num_passengers * 750
    else:
        fare = num_passengers * 300
else:
    fare = num_passengers * 2000

text += f"Total Fare in INR: {fare}\n"
print("\nPassenger Details:")
for p in passenger_list:
    text += f"- Name: {p['name']}\nAge: {p['age']}\n"

text += """\n       Thank you for booking with TWARC!      """
print(text)
with open("ticket.txt", "w", encoding="utf-8") as file:
    file.write(text.strip())

print("\nTicket successfully saved to 'ticket.txt!")
