from tkinter import *
from tkinter.font import Font


def some_function():
    popcorn = sp_1.get()
    mms = sp_2.get()
    pita_chips = sp_3.get()
    orange_juice = sp_4.get()
    water = sp_5.get()
    if popcorn == "0" and mms == "0" and pita_chips == "0" and orange_juice == "0" and water == "0":
        print("\033[3mYou have not chosen any snacks\033[0m\n")
    else:
        print("\033[1mSnacks chosen:\033[0m\nPopcorn: {}\nM&M's: {}\nPita chips: {}\nOrange Juice: {}\nWater: {}"
          .format(popcorn, mms, pita_chips, orange_juice, water))
    root.destroy()


root = Tk()

root.title("Choose your snacks")
root.geometry("350x600")

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


btn = Button(root, text="Confirm", command=some_function)
btn.pack(side="bottom", pady=30)


root.mainloop()
