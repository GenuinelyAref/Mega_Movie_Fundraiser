# Yes / no checker


def yes_no_checker(question, proceed_affirmative, proceed_negative, error_message):
    valid_two = False
    while not valid_two:
        answer = input(question)
        answer = answer.lower()
        if answer[0] == "y":
            return proceed_affirmative
        elif answer[0] == "n":
            return proceed_negative
        else:
            print(error_message)


for i in range(0, 9):
    snacks = yes_no_checker("\nDo you want to order snacks? ", "\033[3mSnacks\033[0m ✔", "\033[3mSnacks\033[0m ❌",
                            "\033[3mThat's not a valid answer. Choose either yes or no\033[0m")
    print(snacks)