# Import tkinter library
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame or window
win = Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
# Set the geometry of tkinter frame
win.geometry(str(screen_width) + "x" + str(screen_height))

win.wait_visibility(win)
win.wm_attributes('-alpha', 0.1)
win.resizable(False, False)


def callback(event):
    win.destroy()


# Create a Label and a Button widget
label = ttk.Label(win, text="Press Enter to Stop operation the Window", font=('Century 17 bold'))
label.pack(ipadx=10)
win.bind('<Return>', callback)
# Disable the Mouse Pointer
win.config(cursor="none")

# Create transparent window


win.mainloop()
