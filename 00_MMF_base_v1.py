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


# *********** Main Routine ***********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# >>>> Get name (can't be blank)
name = not_blank("What is your name? ", "Sorry, that's an invalid input. Please enter your name")

# >>>> Get age (between 12 and 130)

# >>>> Calculate ticket price

# >>>> Loop to ask for snacks

# >>>> Calculate snack price

# >>>> ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file
