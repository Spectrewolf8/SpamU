import tkinter
from tkinter import ttk

import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

win = customtkinter.CTk()
win.geometry("780x400")
win.title("SpamU")


def button_callback():
    print("Button click")
    win.attributes('-zoomed', True)
    win.wm_attributes('-alpha', 0.3)
    win.attributes('-fullscreen', True)
    win.resizable(False, False)

    # Create a Label and a Button widget
    label = ttk.Label(win, text="Press Enter to Stop operation", font=('Century 17 bold'))
    label.pack(ipadx=10)
    win.bind('<Return>', lambda x: callback(label))
    # Disable the Mouse Pointer
    win.config(cursor="none")


# main frame
frame_1 = customtkinter.CTkFrame(master=win)
frame_1.pack(pady=15, padx=60, fill="both", expand=True)

# Text to spam text box label
spamTextBox = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
spamTextBox.place(x=80, y=80)
spamTextBox.insert("0.0", "Your Text Comes Here!\n\n\n\n")
# Text to spam text box
spamTextBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Text to Spam:",
                                          font=customtkinter.CTkFont(size=14, weight="bold"),
                                          justify=customtkinter.CENTER)
spamTextBoxLabel.place(x=80, y=50)


# Wait till start entry box
waitTimeTillStartingSpamEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
waitTimeTillStartingSpamEntryBox.place(x=170, y=170)
# Wait till start entry box label
waitTimeTillStartingSpamEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay before\nStart:",
                                                               font=customtkinter.CTkFont(size=12, weight="normal"),
                                                               justify=customtkinter.CENTER)
waitTimeTillStartingSpamEntryBoxLabel.place(x=80, y=170)


# number of texts to spam entry box
numberOfTextsToSendEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(number)")
numberOfTextsToSendEntryBox.place(x=170, y=210)
# number of texts to spam entry box label
numberOfTextsToSendEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Number of\ntexts to spam:",
                                                          font=customtkinter.CTkFont(size=12, weight="normal"),
                                                          justify=customtkinter.CENTER)
numberOfTextsToSendEntryBoxLabel.place(x=80, y=210)


# delay time between each text sent entry box
delayTimeBetweenEachTextSentEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
delayTimeBetweenEachTextSentEntryBox.place(x=170, y=250)
# delay time between each text sent entry box label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay between\neach text:",
                                                                   font=customtkinter.CTkFont(size=12, weight="normal"),
                                                                   justify=customtkinter.CENTER)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=80, y=250)

# hint
# delay time between each text sent entry box hint label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1,
                                                                   text="🔰 Delay between each\ntext can be in decimal",
                                                                   font=customtkinter.CTkFont(size=8, weight="bold"),
                                                                   justify=customtkinter.CENTER)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=175, y=280)

##########################
# spam progress bar
progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)


# start spamming button
startSpammingButton = customtkinter.CTkButton(master=frame_1, command=button_callback)
startSpammingButton.pack(pady=10, padx=10)

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)


def callback(label):
    win.attributes('-zoomed', False)
    win.wm_attributes('-alpha', 1)
    win.attributes('-fullscreen', False)
    win.geometry("780x400")
    win.resizable(True, True)

    win.config(cursor="arrow")
    label.destroy()
    # win.destroy()


# Create transparent window


win.mainloop()
