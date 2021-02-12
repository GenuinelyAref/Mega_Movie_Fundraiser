# Component 1B: Not-blank custom function


# Function checks for blank input and gives custom error message
def not_blank(prompt, error_message):
    # Take input
    response = input(prompt)
    # strip built-in function removes all leading and trailing spaces to check for actual characters
    while not response.strip(" "):
        # Keep re-taking input until it is no longer blank
        response = input("\n" + error_message + "\n" + prompt)
    return response


# Main routine
name = not_blank("What is your name? ", "Sorry, that's an invalid input. Please enter your name")
