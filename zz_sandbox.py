import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing(window_type):
    messagebox.showinfo("Choose {}".format(window_type), "Please choose your {} then push CONFIRM".format(window_type))

root.protocol("WM_DELETE_WINDOW", on_closing("snacks"))
root.mainloop()
