# Component 3B: Age input & checker (visual edits and commenting complete)


# Number and integer checking function
def int_check(text, lower_bound, upper_bound):
    try:
        # Convert to integer
        number = int(text)
        # If number is higher than lower boundary
        if lower_bound <= number:
            # If number is lower than upper boundary
            if number <= upper_bound:
                # User can proceed to purchasing ticket
                return ["You are eligible to buy a ticket.", True]
            else:
                # User is too old
                return ["You are too old - please contact administration for further enquiries.", False]
        else:
            # User is too young
            return ["You are too young.", False]
    except ValueError:
        # Input is either pure string or float
        return ["Please enter your age (as a whole number)", False]

valid = False
while not valid:
    age_raw = input("\033[1mAge: \033[0m")
    result = int_check(age_raw, 12, 130)
    valid = result[1]
    print("\033[3m" + result[0] + "\033[0m\n")
