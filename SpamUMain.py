from tkinter import ttk

import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

win = customtkinter.CTk()
win.geometry("780x400")
win.title("SpamU")


def button_callback():
    print("Button click")
    win.wait_visibility(win)
    win.wm_attributes('-alpha', 0.3)
    win.attributes('-fullscreen', True)

    win.resizable(False, False)


frame_1 = customtkinter.CTkFrame(master=win)
frame_1.pack(pady=15, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)


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
