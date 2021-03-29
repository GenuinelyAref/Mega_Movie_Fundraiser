# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

# list of surcharge values for all users to print pandas table
surcharge_total = []


def turn_on_button():
    btn['state'] = tk.NORMAL


def output_surcharge():
    # Retrieve surcharge input from tkinter popup
    surcharge = v.get()
    # User chose credit
    if surcharge == 1:
        print("You chose credit - 5% surcharge applies")
        surcharge = 0.05
    # User chose cash
    elif surcharge == 2:
        print("You chose cash - no surcharge applied")
        surcharge = 0
    # Add surcharge value (0 if none) to list for printing in pandas table
    surcharge_total.append(surcharge)
    # Close popup when finished
    root.destroy()


# Creating root Tkinter window
root = Tk()
# Dimensions of window
root.geometry('150x250')
# Title of popup window
root.title("")

# Tkinter integer variable - able to store any integer value
v = IntVar()

# Style class to add style to Radiobutton - it can be used to style any ttk widget
style = Style(root)
style.configure("TRadiobutton", font=("arial", 12, "bold"))
style.configure("TLabel", font=("arial", 15, "bold"))

#  Print header
w = Label(root, text="Payment\n method")
w.pack()

# Confirm option
btn = Button(root, text="Confirm", state=tk.DISABLED, command=output_surcharge)
btn.pack(side="bottom", pady=30)

sp_1 = Spinbox(root)
sp_1.pack()

# Credit option
radio_one = Radiobutton(root, text="Credit", variable=v, value=1, command=turn_on_button).pack(side="top", pady=25)
# Cash option
radio_two = Radiobutton(root, text="Cash", variable=v, value=2, command=turn_on_button).pack(side="top", pady=0)


mainloop()
