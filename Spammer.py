import os
import time
from tkinter import END

import pyautogui as pt
from pyperclip import copy as copyToClipboard


class Spammer:
    def __init__(self, numberOfTextsToSend, delayTimeBetweenEachTextSent):
        self.numberOfTextsToSend = numberOfTextsToSend
        self.breakOperation = False
        self.delayTimeBetweenEachTextSent = delayTimeBetweenEachTextSent

    def breakOperationCall(self):
        self.breakOperation = True

    def startOperation(self, message, statusBox, win):
        os.system("xhost +")
        # to workaround Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'Authorization required,
        # but no authorization protocol specified\n' on linux

        copyToClipboard((str(message)).strip())
        initialTime = time.time()
        i = 1
        while i <= self.numberOfTextsToSend:
            if self.breakOperation:
                break
            pt.hotkey('ctrl', 'v')
            pt.press("enter")
            print("spammed", i, "th message")
            statusBox.delete("0.0", END)
            statusBox.insert("0.0", "spammed " + str(i) + "th message")
            win.update()

            time.sleep(self.delayTimeBetweenEachTextSent)
            i += 1
            finalTime = time.time()

        print()
        statusBox.delete("0.0", END)
        statusBox.insert("0.0", "spammed " + str(i) + " messages in " + str(finalTime - initialTime))
        win.update()
