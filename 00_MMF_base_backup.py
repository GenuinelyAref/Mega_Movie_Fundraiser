# import statements


# Function checks for blank input
def not_blank(prompt, error_message):
    # Take input
    response = input(prompt)
    # strip built-in function removes all leading and trailing spaces to check for actual characters
    while not response.strip(" "):
        # Keep re-taking input until it is no longer blank
        response = input("\n" + error_message + "\n" + prompt)
    return response


# Integer checking function
def int_check(text, lower_bound, upper_bound, too_low_error, too_high_error, conversion_error, affirmative_message):
    try:
        # Convert to integer
        number = int(text)
        # If number is higher than lower boundary
        if lower_bound <= number:
            # if number is lower than upper boundary
            if number <= upper_bound:
                # number is within boundaries
                return [affirmative_message, True, 3, number]
            else:
                # number is higher than upper boundary
                return [too_high_error, False, 1]
        else:
            # number is lower than lower boundary
            return [too_low_error, False, 1]
    except ValueError:
        # Input is either pure string or float
        return [conversion_error, False, 2]


# experimental constants
# Initial number of tickets
TICKETS = 5
# Number of tickets sold per sale
TICKETS_SOLD = 1

# Ready-to-use variables
result = []
ticket_sales = 0


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
        ticket_profit = ticket_sales - (5*(TICKETS - tickets))
        print("\nTickets sold: {}\nTickets left: {}\n"
              "Ticket sales = ${:.2f}\nTicket profit = ${:.2f}"
              "".format(TICKETS - tickets, tickets, ticket_sales, ticket_profit))
        break
    valid = False
    while not valid:
        age_raw = input("\033[1mAge: \033[0m")
        result = int_check(age_raw, 12, 130, "You are too young.",
                           "You are too old - please contact administration for "
                           "further enquiries.", "Please enter your age (as a whole number)",
                           "You are eligible to buy a ticket.")
        print("\033[3m" + result[0] + "\033[0m\n")
        if result[2] == 2:
            valid = False
        elif result[2] == 3:
            age = result[3]
            # Children/teens
            if 12 <= age <= 15:
                ticket_price = 7.5
            # Adults
            elif 16 <= age <= 64:
                ticket_price = 10.5
            # Seniors
            else:
                ticket_price = 6.5
            # Print ticket price
            ticket_sales += ticket_price
            print("Ticket price = ${:.2f}\n".format(ticket_price))
            valid = True
        else:
            valid = True
    else:
        if result[2] == 3:
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

    # >>>> Loop to ask for snacks

    # >>>> Calculate snack price

    # >>>> ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file
