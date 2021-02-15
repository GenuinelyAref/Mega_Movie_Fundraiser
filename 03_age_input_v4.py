# Component 3D: Age input & checker (break loop if value is too high or too low)


# Number and integer checking function
def int_check(text, lower_bound, upper_bound, too_low_error, too_high_error, conversion_error, affirmative_message):
    try:
        # Convert to integer
        number = int(text)
        # If number is higher than lower boundary
        if lower_bound <= number:
            # if number is lower than upper boundary
            if number <= upper_bound:
                # number is within boundaries
                return [affirmative_message, True, 3]
            else:
                # number is higher than upper boundary
                return [too_high_error, False, 1]
        else:
            # number is lower than lower boundary
            return [too_low_error, False, 1]
    except ValueError:
        # Input is either pure string or float
        return [conversion_error, False, 2]


valid = False
while not valid:
    age_raw = input("\033[1mAge: \033[0m")
    result = int_check(age_raw, 12, 130, "You are too young.", "You are too old - please contact administration for "
                                         "further enquiries.", "Please enter your age (as a whole number)", "You are "
                                         "eligible to buy a ticket.")
    valid = result[1]
    print("\033[3m" + result[0] + "\033[0m\n")
