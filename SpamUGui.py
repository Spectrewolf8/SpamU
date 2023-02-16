from tkinter import ttk

import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

win = customtkinter.CTk()
win.geometry("620x500")
win.title("SpamU")

# main frame
frame_1 = customtkinter.CTkFrame(master=win)
frame_1.pack(pady=15, padx=60, fill="both", expand=True)

# Text to spam text box
spamTextBox = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
spamTextBox.place(x=80, y=50)
spamTextBox.insert("0.0", "Your Text Comes Here!\n\n\n\n")
# Text to spam text box label
spamTextBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Text to Spam:",
                                          font=customtkinter.CTkFont(size=14, weight="bold"),
                                          justify=customtkinter.CENTER)
spamTextBoxLabel.place(x=80, y=20)

# spam parameters
# Wait till start entry box
waitTimeTillStartingSpamEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
waitTimeTillStartingSpamEntryBox.place(x=170, y=140)
# Wait till start entry box label
waitTimeTillStartingSpamEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay before\nStart:",
                                                               font=customtkinter.CTkFont(size=13, weight="normal"),
                                                               justify=customtkinter.LEFT)
waitTimeTillStartingSpamEntryBoxLabel.place(x=80, y=140)

# number of texts to spam entry box
numberOfTextsToSendEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(number)")
numberOfTextsToSendEntryBox.place(x=170, y=180)
# number of texts to spam entry box label
numberOfTextsToSendEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Number of\ntexts to spam:",
                                                          font=customtkinter.CTkFont(size=13, weight="normal"),
                                                          justify=customtkinter.LEFT)
numberOfTextsToSendEntryBoxLabel.place(x=80, y=180)

# delay time between each text sent entry box
delayTimeBetweenEachTextSentEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
delayTimeBetweenEachTextSentEntryBox.place(x=170, y=220)
# delay time between each text sent entry box label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay between\neach text:",
                                                                   font=customtkinter.CTkFont(size=13, weight="normal"),
                                                                   justify=customtkinter.LEFT)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=80, y=220)

# hint
# delay time between each text sent entry box hint label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1,
                                                                   text="🔰 Delay between each\ntext can be in decimal",
                                                                   font=customtkinter.CTkFont(size=10, weight="normal"),
                                                                   justify=customtkinter.CENTER)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=170, y=250)

##########################

# safe mode check box
safeModeCheckBox = customtkinter.CTkCheckBox(master=frame_1, checkbox_height=20,
                                             text="Safe Mode",
                                             font=customtkinter.CTkFont(size=16, weight="normal"))
safeModeCheckBox.place(x=120, y=300)
safeModeCheckBox.select()


# start spamming button callback
def startSpammingButton_callback():
    print("Spam Started")
    win.attributes('-zoomed', True)
    win.wm_attributes('-alpha', 0.3)
    win.attributes('-fullscreen', True)
    win.resizable(False, False)

    # Create a Label and a Button widget
    pressEnterToExitLabel = ttk.Label(win, text="Press Enter to Stop operation", font=('Century 17 bold'))
    pressEnterToExitLabel.pack(ipadx=10)
    win.bind('<Return>', lambda x: exitOnEnter_callback(pressEnterToExitLabel))
    # Disable the Mouse Pointer
    win.config(cursor="none")


def exitOnEnter_callback(label):
    win.attributes('-zoomed', False)
    win.wm_attributes('-alpha', 1)
    win.attributes('-fullscreen', False)
    win.geometry("620x500")
    win.resizable(True, True)

    win.config(cursor="arrow")
    label.destroy()


# start spamming button
startSpammingButton = customtkinter.CTkButton(master=frame_1, command=startSpammingButton_callback,
                                              text="Start Spam!",
                                              font=customtkinter.CTkFont(size=14, weight="normal"))
startSpammingButton.place(x=100, y=330)
410
# spam progress bar
spamProgressBar = customtkinter.CTkProgressBar(master=frame_1, width=180)
spamProgressBar.place(x=80, y=400)
spamProgressBar.set(0)

# spam progress bar label
spamProgressBarLabel = customtkinter.CTkLabel(master=frame_1, text="Progress:",
                                              font=customtkinter.CTkFont(size=12, weight="bold"),
                                              justify=customtkinter.LEFT)
spamProgressBarLabel.place(x=80, y=370)

# Status label
statusLabel = customtkinter.CTkLabel(master=frame_1, text="Status:",
                                     font=customtkinter.CTkFont(size=14, weight="bold"),
                                     justify=customtkinter.CENTER)
statusLabel.place(x=80, y=410)

# guide label
guideLabel = customtkinter.CTkLabel(master=frame_1,
                                    text="Defaults:\n  delayBeforeStart - 15s\n  numberOfTextsToSpam - "
                                         "50\n  delayBetweenEachText - 1s\n\n\n\n\n\n\n\n""Safe mode: disable "
                                         "interactions till"
                                         "operation completion ("
                                         "recommended)",
                                    font=customtkinter.CTkFont(size=12, weight="normal"),
                                    justify=customtkinter.LEFT, wraplength=165)
guideLabel.place(x=320, y=140)

win.mainloop()
