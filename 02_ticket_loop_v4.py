# Component 2C: Loop component (Visual edits)

# Set initial number of tickets as a constant
TICKETS = 5
TICKETS_SOLD = 1
tickets = TICKETS


# Keeps selling tickets until they run out
while tickets > 0:
    name = input("\033[1mName: \033[0m")
    # Exit code
    if name == "xxx":
        # Stop sales then give sales information
        print("\nTickets sold: {}\nTickets left: {}".format(TICKETS - tickets, tickets))
        break
    else:
        # Reduce one ticket from total
        tickets -= TICKETS_SOLD
        # Tells user how many tickets were sold (useful for later on)
        if TICKETS_SOLD == 1:
            # Ticket rather than ticket"s"
            plural = ""
        else:
            # Plural for ticket"s"
            plural = "s"
        print("\033[3mSold {} ticket{} to \"{}\"\033[0m".format(TICKETS_SOLD, plural, name))
        # No more tickets available
        if tickets == 0:
            print("All tickets have been sold, no more are available.")
        # Warn user when there is only one ticket left
        elif tickets == 1:
            print("*** Only ONE ticket left ***\n")
        # Give user number of tickets left
        else:
            print("Ticket(s) left: {}\n".format(tickets))
