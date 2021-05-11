# import statements
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
import pandas


# Snack summary data - collects data and calculates totals
def snacks_tool(a, b, c, d, e):
    snack_payment = (a*a_price) + (b*b_price) + (c*c_price) + (d*d_price) + (e*e_price)
    user_snack_profit = snack_payment * snack_profit_percentage
    return [snack_payment, user_snack_profit]


# Takes and processes snack data from tkinter popup
def output_data():
    chosen_popcorn = int(sp_1.get())
    chosen_mms = int(sp_2.get())
    chosen_pita_chips = int(sp_3.get())
    chosen_orange_juice = int(sp_4.get())
    chosen_water = int(sp_5.get())
    user_snack_temp_list = snacks_tool(chosen_popcorn, chosen_mms, chosen_pita_chips, chosen_orange_juice, chosen_water)
    if chosen_popcorn == 0 and chosen_mms == 0 and chosen_pita_chips == 0 and chosen_orange_juice == 0 and\
            chosen_water == 0:
        print("\033[3mYou have not chosen any snacks\033[0m\n")
    else:
        print("\033[1m\nSnacks chosen:\033[0m\nPopcorn: {}\nM&M's: {}\nPita chips: {}\nOrange Juice: {}\nWater: {}".
              format(chosen_popcorn, chosen_mms, chosen_pita_chips, chosen_orange_juice, chosen_water))
        print("\nSnacks price: ${:.2f}".format(user_snack_temp_list[0]))
    popcorn_total.append(chosen_popcorn)
    mms_total.append(chosen_mms)
    pita_chips_total.append(chosen_pita_chips)
    orange_juice_total.append(chosen_orange_juice)
    water_total.append(chosen_water)
    snack_profit.append(user_snack_temp_list[1])
    root.destroy()


# Generic yes/no checking function
def yes_no_checker(question, error_message):
    valid_two = False
    while not valid_two:
        answer = input(question)
        answer = answer.lower()
        try:
            if answer[0] == "y":
                return "Yes"
            elif answer[0] == "n":
                return "No"
            else:
                print(error_message)
        except IndexError:
            print(error_message)


# Asks user for surcharge option and adds the surcharge value if any
def output_surcharge():
    # Retrieve surcharge input from tkinter popup
    surcharge = v.get()
    # User chose credit
    if surcharge == 1:
        print("You chose credit - 5% surcharge applies")
        surcharge = 0.05
    # User chose cash
    elif surcharge == 2:
        print("You chose cash - no surcharge applied")
        surcharge = 0
    # Add surcharge value (0 if none) to list for printing in pandas table
    surcharge_total.append(surcharge)
    # Close popup when finished
    root.destroy()


# Function that formats a numeric value in monetary format ($x.xx)
def monetize(number):
    return "${:.2f}".format(float(number))


# Function to enable "confirm" button in surcharge popup window
def turn_on_button():
    btn['state'] = tk.NORMAL


# Function to prevent forced closure of tkinter snack window (eg Alt + F4)
def prevent_closing_snacks():
    messagebox.showinfo("Choose snacks", "Please choose your snacks then push CONFIRM")
    pass


# Function to prevent forced closure of tkinter surcharge window (eg Alt + F4)
def prevent_closing_payment_method():
    messagebox.showinfo("Choose payment method", "Please choose your payment method then push CONFIRM")
    pass


# Function checks for blank input
def not_blank(prompt, error_message):
    # Take input
    response = input(prompt)
    # strip built-in function removes all leading and trailing spaces to check for actual characters
    while not response.strip(" "):
        # Keep re-taking input until it is no longer blank
        response = input("\n" + error_message + "\n" + prompt)
    return response


# Function that displays/hides instructions
def instructions():
    print("\033[1mWelcome to Mega Movie Fundraiser\033[0m\n\n")
    instructions_text = "\n\033[1m<<Introduction>>\033[0m\nTo buy a ticket for the movie fundraiser ," \
                        " you will need to provide your name, age, choice of snacks and payment method." \
                        "\nPlease enter your real name and age, as your identity could be confirmed upon request." \
                        " We thank you for supporting the\ncause and hope that you enjoy the movie."
    reply = yes_no_checker("Have you used this program before?\nYes or no: ",
                           "\033[3mThat's not a valid answer. Choose either yes or no\033[0m\n")
    if reply == "No":
        print(instructions_text)
    else:
        pass


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


# CONSTANTS
# Initial number of tickets
TICKETS = 9
# Number of tickets sold per sale
TICKETS_SOLD = 1
# Cost of each ticket
ticket_cost = 5
# Profit percentage on all snacks = 20%
snack_profit_percentage = 0.2
# Snack prices
a_price = 2.5
b_price = 3
c_price = 4.5
d_price = 3.25
e_price = 2

# LISTS
result = []
# Total of each snack for pandas data dictionary
all_names = []
all_tickets = []

# Lists for snacks
popcorn_total = []
mms_total = []
pita_chips_total = []
orange_juice_total = []
water_total = []

# Calculation column lists
surcharge_total = []
snack_profit = []
ticket_profit_list = []
total_profit = []
totals = []
totals_updated = []

# VARIABLES
# Naming constants to remove error
total_snack_profit = 0
popcorn = 0
mms = 0
pita_chips = 0
orange_juice = 0
water = 0
# Other variables
ticket_sales = 0
ticket_price = 0
total_ticket_profit = 0


# DICTIONARIES
# Snacks prices
snack_prices_dict = {
    "Popcorn": 2.5,
    "M&M's": 3,
    "Pita chips": 4.5,
    "Orange juice": 3.25,
    "Water": 2,
}

# Main data frame
movie_data_dict = {
    "Name": all_names,
    "Ticket price": all_tickets,
    "Popcorn": popcorn_total,
    "M&M's": mms_total,
    "Pita chips": pita_chips_total,
    "Orange juice": orange_juice_total,
    "Water": water_total,
}

# Profit data frame
profit_summary = {
    "Name": all_names,
    "Snack profit": snack_profit,
    "Ticket profit": ticket_profit_list,
    "Total profit": total_profit,
}

# Totals data frame
totals_summary = {
    "Item": ["Popcorn", "M&M's", "Pita Chips", "Orange Juice", "Water", "Total snack profit", "Total ticket profit",
             "Total profit"],
    "Amount": totals,
}


# *********** Main Routine ***********

# Ask user if they have used the program before & show instructions if necessary
instructions()

# Loop to get ticket details
# Keeps selling tickets until they run out
tickets = TICKETS
# Keep selling tickets if there are any left
while tickets > 0:
    # Ask for name
    name = not_blank("\n\033[1mName: \033[0m", "Sorry, that's an invalid input. Please enter your name")
    # Exit code for summary data
    if name == "xxx":
        # Stop sales then give sales information
        ticket_profit = sum(ticket_profit_list)
        print("\nTickets sold: {}\nTickets left: {}\n"
              "Ticket sales = ${:.2f}\nTicket profit = ${:.2f}"
              "".format(TICKETS - tickets, tickets, ticket_sales, ticket_profit))
        break
    valid = False
    # When name is not blank
    while not valid:
        # Ask for age
        age_raw = input("\033[1mAge: \033[0m")
        result = int_check(age_raw, 12, 130, "You are too young.",
                           "You are too old - please contact administration for "
                           "further enquiries.", "Please enter your age (as a whole number)",
                           "You are eligible to buy a ticket.")
        print("\033[3m" + result[0] + "\033[0m\n")
        # If age is invalid
        if result[2] == 2:
            valid = False
        # If age is valid
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
            ticket_profit_list.append(ticket_price-5)
            print("Ticket price = ${:.2f}\n".format(ticket_price))
            valid = True
        else:
            valid = True
    else:
        if result[2] == 3:
            # Check if user wants snacks
            snacks = yes_no_checker("\nDo you want to order snacks? ",
                                    "\033[3mThat's not a valid answer. Choose either yes or no\033[0m")
            # If user wants snack(s)
            if snacks == "Yes":
                print("You chose \"{}\" - a pop-up will open up shortly".format(snacks))
                # ~~~ TKINTER POPUP WINDOW ~~~ for snacks
                # Create window
                root = Tk()
                # Window title
                root.title("Choose your snacks")
                # Window size
                root.geometry("350x600")
                # Bring window to front layer on screen
                root.lift()
                root.attributes("-topmost", True)
                root.attributes("-topmost", False)

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
                sp_1 = Spinbox(root, from_=0, to=5, width=2, state="readonly",
                               font=Font(family="Helvetica", weight="bold", size=20,))
                sp_1.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # M&M's
                w = Label(root, text="M&M's - $3.00 each", font="50")
                w.pack()
                sp_2 = Spinbox(root, from_=0, to=5, width=2, state="readonly",
                               font=Font(family="Helvetica", weight="bold", size=20))
                sp_2.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Pita chips
                w = Label(root, text="Pita chips - $4.50 each", font="50")
                w.pack()
                sp_3 = Spinbox(root, from_=0, to=5, width=2, state="readonly",
                               font=Font(family="Helvetica", weight="bold", size=20))
                sp_3.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Orange Juice
                w = Label(root, text="Orange juice - $3.25 each", font="50")
                w.pack()
                sp_4 = Spinbox(root, from_=0, to=5, width=2, state="readonly",
                               font=Font(family="Helvetica", weight="bold", size=20))
                sp_4.pack()

                # Blank line
                x = Label(root, text="", font="50")
                x.pack()

                # Water
                w = Label(root, text="Water - $2.00 each", font="50")
                w.pack()
                sp_5 = Spinbox(root, from_=0, to=5, width=2, state="readonly",
                               font=Font(family="Helvetica", weight="bold", size=20))
                sp_5.pack()

                # Confirm button
                btn = Button(root, text="CONFIRM", command=output_data)
                btn.pack(side="bottom", pady=30)
                # Prevent forced closure of window
                root.protocol("WM_DELETE_WINDOW", prevent_closing_snacks)
                # Iterate popup window code
                root.mainloop()
            # If user does not want snacks
            elif snacks == "No":
                print("\033[3mSkipping snacks\033[0m")
                # Set all snack values to 0
                popcorn_total.append(0)
                mms_total.append(0)
                pita_chips_total.append(0)
                orange_juice_total.append(0)
                water_total.append(0)
                snack_profit.append(0)

            # ~~~ TKINTER POPUP WINDOW ~~~ for surcharge
            # Create window
            root = Tk()
            # Window size
            root.geometry('150x250')
            # Window title
            root.title("")
            # Bring window to front layer on screen
            root.lift()
            root.attributes("-topmost", True)
            root.attributes("-topmost", False)

            # Tkinter integer variable - able to store any integer value
            v = IntVar()

            #  Print header
            w = Label(root, text="Payment\n method", font=("arial", 15, "bold"))
            w.pack()

            # Confirm option
            btn = Button(root, text="CONFIRM", state=tk.DISABLED, command=output_surcharge)
            btn.pack(side="bottom", pady=30)

            # Credit option
            radio_one = Radiobutton(root, text="Credit", variable=v, value=1, command=turn_on_button,
                                    font=("arial", 12, "bold")).pack(side="top", pady=25)
            # Cash option
            radio_two = Radiobutton(root, text="Cash", variable=v, value=2, command=turn_on_button,
                                    font=("arial", 12, "bold")).pack(side="top", pady=0)

            # Prevent forced closure of window
            root.protocol("WM_DELETE_WINDOW", prevent_closing_payment_method)
            # Iterate popup window code
            root.mainloop()

            # Reduce one ticket from total
            tickets -= TICKETS_SOLD
            # Tells user how many tickets were sold
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
            total_profit.append((ticket_price - 5) + snack_profit[-1])
        # Collect data for spreadsheet
        all_names.append(name)
        all_tickets.append(ticket_price)


# Create dataframe of ticket details for each user
movie_frame = pandas.DataFrame(movie_data_dict)
# Sort dataframe columns by Name column (first column)
movie_frame = movie_frame.set_index("Name")

# Add column for snacks cost for each user
movie_frame["Snacks cost"] = (movie_frame["Popcorn"]*snack_prices_dict["Popcorn"]) + \
    (movie_frame["M&M's"]*snack_prices_dict["M&M's"]) + \
    (movie_frame["Pita chips"]*snack_prices_dict["Pita chips"]) + \
    (movie_frame["Orange juice"]*snack_prices_dict["Orange juice"]) + \
    (movie_frame["Water"]*snack_prices_dict["Water"])

# Add column for sub-total value for each user
movie_frame["Sub-total"] = movie_frame["Ticket price"] + movie_frame["Snacks cost"]
# Add column for surcharge value for each user
movie_frame["Surcharge"] = round(surcharge_total*movie_frame["Sub-total"], 2)
# Add column for total value for each user
movie_frame["Total"] = movie_frame["Surcharge"] + movie_frame["Sub-total"]

# Turn relevant dataframe values into monetary format
movie_frame_list = ["Ticket price", "Snacks cost", "Sub-total", "Surcharge", "Total"]
for h in movie_frame_list:
    movie_frame[h] = movie_frame[h].apply(monetize)

# Display all columns in the dataframe
pandas.set_option("display.max_columns", None)
# Display all columns in one line
pandas.set_option("expand_frame_repr", False)

# Add total values to total data list
totals.extend([sum(popcorn_total), sum(mms_total), sum(pita_chips_total), sum(orange_juice_total), sum(water_total),
               sum(snack_profit), sum(ticket_profit_list), sum(total_profit)])
# Create total data summary dataframe
summary_frame = pandas.DataFrame(totals_summary)
# Sort columns in dataframe by Item column (first column)
summary_frame = summary_frame.set_index("Item")

# Monetize appropriate values in totals dataframe
for i in range(0, 5):
    totals_updated.append(totals[i])
for j in range(5, 8):
    n = str(summary_frame["Amount"][j])
    n = n.strip("$")
    n = monetize(n)
    totals_updated.append(n)
summary_frame["Amount"] = totals_updated

# Create dataframe for profit values per user
profit_frame = pandas.DataFrame(profit_summary)
# Sort columns in dataframe by Name column (first column)
profit_frame = profit_frame.set_index("Name")

# Monetize appropriate values in profit dataframe
profit_frame_list = ["Snack profit", "Ticket profit", "Total profit"]
for k in profit_frame_list:
    profit_frame[k] = profit_frame[k].apply(monetize)

# Print user ticket information dataframe
print("\n\033[1mTICKET INFO\033[0m\n")
print(movie_frame)
# Print profit information dataframe
print("\n\033[1mPROFIT INFO\033[0m\n")
print(profit_frame)
# Print totals summary dataframe
print("\n\033[1mSUMMARY INFO\033[0m\n")
print(summary_frame)

# Output data to separate text files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("totals_summary.csv")
profit_frame.to_csv("individual_profits.csv")
