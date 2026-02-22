THEATRE_CAPACITY = 350

remaining_seats = THEATRE_CAPACITY
total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while remaining_seats > 0:
    print(f"\nSeats Left: {remaining_seats}")
    tickets = int(input("Enter number of tickets (0 to exit): "))

    if tickets == 0:
        print("\nBooking stopped by user.")
        break


    if tickets < 1 or tickets > 15:
        print("Invalid ticket count! Must be between 1 and 15.")
        continue  


    if tickets > remaining_seats:
        print("Not enough seats available!")
        continue

    total_bookings += 1


    age_list = []
    for i in range(tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        age_list.append(age)


    invalid_age_found = False
    for age in age_list:
        if age < 12:
            invalid_age_found = True
            break

    if invalid_age_found:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
        continue


    print(f"BOOKING CONFIRMED - {tickets} tickets")
    tickets_sold += tickets
    remaining_seats -= tickets


    if remaining_seats == 0:
        print("\nTheatre Full! No more bookings allowed.")
        break


print("\n========== FINAL REPORT ==========")
print(f"Total Bookings Attempted : {total_bookings}")
print(f"Total Tickets Sold       : {tickets_sold}")
print(f"Rejected Bookings        : {rejected_bookings}")
print(f"Remaining Seats          : {remaining_seats}")
