import tkinter as tk


root=tk.Tk()
root.overrideredirect(True)

def close_program():
    root.destroy()

def disable_event():
    pass

btn = tk.Button(root, text = "Click me to close", command = close_program)
btn.pack()

root.protocol("WM_DELETE_WINDOW", disable_event)

root.mainloop()