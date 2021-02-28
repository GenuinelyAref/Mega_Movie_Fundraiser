from tkinter import *
from tkinter.font import Font


def some_function():
    a = sp_1.get()
    b = sp_2.get()
    c = sp_3.get()
    d = sp_4.get()
    e = sp_5.get()
    print("\033[1mSnacks chosen:\033[0m\nPopcorn: {}\nM&M's: {}\nPita chips: {}\nOrange Juice: {}\nWater: {}"
          .format(a, b, c, d, e))
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
