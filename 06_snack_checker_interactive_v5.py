# Same as v3 but

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
        print("\033[1mSnacks chosen:\033[0m\nPopcorn: {}\nM&M's: {}\nPita chips: {}\nOrange Juice: {}\nWater: {}"
          .format(popcorn, mms, pita_chips, orange_juice, water))
        user_snack_temp_list = snacks_tool(popcorn, mms, pita_chips, orange_juice, water, total_snack_profit)
        print("\nSnacks price: ${:.2f}".format(user_snack_temp_list[0]))
    root.destroy()


root = Tk()

root.title("Choose your snacks")
root.geometry("350x600")
root.lift()
root.attributes("-topmost", True)
root.attributes("-topmost", False)

# Title
x = Label(root, text="", font="50")
x.pack()
n = Label(root, text="Choose your snacks:", font=Font(family="Helvetica", weight="bold", size=23), background="red",
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

