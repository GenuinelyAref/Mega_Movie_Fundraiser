# Component 1A: Not-blank function


# Function checks for blank input
def not_blank(prompt):
    # Take input
    response = input(prompt)
    # strip built-in function removes all leading and trailing spaces to check for actual characters
    while not response.strip(" "):
        # Keep re-taking input until it is no longer blank
        response = input("\nSorry, that's an invalid input.\n" + prompt)
    return response


# Main routine
name = not_blank("What is your name? ")
