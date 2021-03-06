# import statements
from tkinter import *
from tkinter.font import Font

snack_profit = 0.2
total_snack_profit = 5
a_price = 2.5
b_price = 3
c_price = 4.5
d_price = 3.25
e_price = 2


def snacks_tool(a, b, c, d, e, current_total):
    snack_payment = (a*a_price) + (b*b_price) + (c*c_price) + (d*d_price) + (e*e_price)
    user_snack_profit = snack_payment*0.2
    current_total += user_snack_profit
    return [snack_payment, user_snack_profit, current_total]


def output_data():
    popcorn = int(sp_1.get())
    mms = int(sp_2.get())
    pita_chips = int(sp_3.get())
    orange_juice = int(sp_4.get())
    water = int(sp_5.get())
    if popcorn == 0 and mms == 0 and pita_chips == 0 and orange_juice == 0 and water == 0:
        print("\033[3mYou have not chosen any snacks\033[0m\n")
    else:
        print("\033[1m\nSnacks chosen:\033[0m\nPopcorn: {}\nM&M's: {}\nPita chips: {}\nOrange Juice: {}\nWater: {}".
              format(popcorn, mms, pita_chips, orange_juice, water))
        user_snack_temp_list = snacks_tool(popcorn, mms, pita_chips, orange_juice, water, total_snack_profit)
        print("\nSnacks price: ${:.2f}".format(user_snack_temp_list[0]))
    root.destroy()


# Generic yes/no checking function
def yes_no_checker(question, error_message):
    valid_two = False
    while not valid_two:
        answer = input(question)
        answer = answer.lower()
        if answer[0] == "y":
            return "Yes"
        elif answer[0] == "n":
            return "No"
        else:
            print(error_message)


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
            # Check if user wants snacks
            snacks = yes_no_checker("\nDo you want to order snacks? ",
                                    "\033[3mThat's not a valid answer. Choose either yes"
                                    " or no\033[0m")
            if snacks == "Yes":
                print("You chose \"{}\" - a pop-up will open up shortly. \033[1mCheck your TASKBAR for the pop-up."
                      "\033[0m".format(snacks))
                # ###############################
                # ###############################
                # ###############################
                # ###############################
                # ###############################
                root = Tk()

                root.title("Choose your snacks")
                root.geometry("350x600")

                # Title
                x = Label(root, text="", font="50")
                x.pack()
                n = Label(root, text="Choose your snacks:", font=Font(family="Helvetica", weight="bold", size=23),
                          background="red",
                          foreground="white")
                n.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Popcorn
                w = Label(root, text="Popcorn - $2.50 each", font="50")
                w.pack()
                sp_1 = Spinbox(root, from_=0, to=5, width=2, font=Font(family="Helvetica", weight="bold", size=20))
                sp_1.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # M&M's
                w = Label(root, text="M&M's - $3.00 each", font="50")
                w.pack()
                sp_2 = Spinbox(root, from_=0, to=5, width=2, font=Font(family="Helvetica", weight="bold", size=20))
                sp_2.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Pita chips
                w = Label(root, text="Pita chips - $4.50 each", font="50")
                w.pack()
                sp_3 = Spinbox(root, from_=0, to=5, width=2, font=Font(family="Helvetica", weight="bold", size=20))
                sp_3.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Orange Juice
                w = Label(root, text="Orange juice - $3.25 each", font="50")
                w.pack()
                sp_4 = Spinbox(root, from_=0, to=5, width=2, font=Font(family="Helvetica", weight="bold", size=20))
                sp_4.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Water
                w = Label(root, text="Water - $2.00 each", font="50")
                w.pack()
                sp_5 = Spinbox(root, from_=0, to=5, width=2, font=Font(family="Helvetica", weight="bold", size=20))
                sp_5.pack()

                btn = Button(root, text="Confirm", command=output_data)
                btn.pack(side="bottom", pady=30)
                root.mainloop()
            elif snacks == "No":
                print("\033[3mSkipping snacks\033[0m")
            # ###############################
            # ###############################
            # ###############################
            # ###############################
            # Reduce one ticket from total
            tickets -= TICKETS_SOLD
            # Tells user how many tickets were sold (useful for later on)
            if TICKETS_SOLD == 1:
                # Ticket rather than ticket"s"
                plural = ""
            else:
                # Plural for ticket"s"
                plural = "s"
            print()
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

    # >>>> Calculate snack price

    # >>>> ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file
