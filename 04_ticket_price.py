# Ticket price calculator

# Repeat program 6 times for testing
for i in range(0, 6):
    # Take age input
    age = int(input("Age: "))
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
    print("Ticket price = ${:.2f}\n".format(ticket_price))
