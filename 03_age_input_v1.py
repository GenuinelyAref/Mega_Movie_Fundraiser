# Component 3A: Age input & checker


# Number and integer checking function
def int_check(text, lower_bound, upper_bound):
    try:
        number = int(text)
        if lower_bound <= number:
            if number <= upper_bound:
                return ["You are eligible to buy a ticket.", True]
            else:
                return ["You are too old.", False]
        else:
            return ["You are too young.", False]
    except ValueError:
        return ["Please enter your age (as a whole number)", False]

valid = False
while not valid:
    age_raw = input("What is your age? ")
    result = int_check(age_raw, 12, 130)
    valid = result[1]
    print(result[0] + "\n")
