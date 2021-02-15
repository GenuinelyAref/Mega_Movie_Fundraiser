# import statements


# functions go here

# Function checks for blank input
def not_blank(prompt, error_message):
    # Take input
    response = input(prompt)
    # strip built-in function removes all leading and trailing spaces to check for actual characters
    while not response.strip(" "):
        # Keep re-taking input until it is no longer blank
        response = input("\n" + error_message + "\n" + prompt)
    return response

# experimental constants
# Initial number of tickets
TICKETS = 5
# Number of tickets sold per sale
TICKETS_SOLD = 1


# *********** Main Routine ***********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details


# Keeps selling tickets until they run out
tickets = TICKETS
while tickets > 0:
    name = not_blank("\033[1mName: \033[0m", "Sorry, that's an invalid input. Please enter your name")
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

    # >>>> Get name (can't be blank)


    # >>>> Get age (between 12 and 130)

    # >>>> Calculate ticket price

    # >>>> Loop to ask for snacks

    # >>>> Calculate snack price

    # >>>> ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file
