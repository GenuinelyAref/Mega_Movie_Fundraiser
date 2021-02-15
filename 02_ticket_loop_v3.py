# Component 2C: Loop component (Shows how many tickets were sold)

# Set initial number of tickets as a constant
TICKETS = 5
TICKETS_SOLD = 1
tickets = TICKETS


# Keeps selling tickets until they run out
while tickets > 0:
    name = input("Name: ")
    # Exit code
    if name == "xxx":
        # Stop sales then give sales information
        print("\nTickets sold: {}\nTickets left: {}".format(TICKETS - tickets, tickets))
        break
    else:
        # Reduce one ticket from total
        tickets -= TICKETS_SOLD
        # Tells user how many tickets were sold (useful for later on)
        print("Sold {} tickets".format(TICKETS_SOLD))
        # No more tickets available
        if tickets == 0:
            print("All tickets have been sold, no more are available.")
        # Warn user when there is only one ticket left
        elif tickets == 1:
            print("*** Only ONE ticket left ***\n")
        # Give user number of tickets left
        else:
            print("Ticket(s) left: {}\n".format(tickets))
