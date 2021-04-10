from tkinter import *

root = Tk()

pressed_f4 = False  # Is Alt-F4 pressed?

def do_exit():
    global pressed_f4
    print('Trying to close application')
    if pressed_f4:  # Deny if Alt-F4 is pressed
        print('Denied!')
        pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application

def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event):  # Exit application
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.bind('<Escape>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)

root.mainloop()
