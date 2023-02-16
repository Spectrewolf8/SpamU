import os
import time

import pyautogui as pt
from pyperclip import copy as copyToClipboard

message2 = "good spam desu desu"


class Spammer:
    def __init__(self, waitTimeBeforeStartingSpam, numberOfTextsToSend, delayTimeBetweenEachTextSent):
        self.waitTimeTillStartingSpam = waitTimeBeforeStartingSpam

        self.numberOfTextsToSend = numberOfTextsToSend

        self.delayTimeBetweenEachTextSent = delayTimeBetweenEachTextSent

    def startOperation(self, message):
        os.system("xhost +")
        # to workaround Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'Authorization required,
        # but no authorization protocol specified\n' on linux
        print("starting spam in", self.waitTimeTillStartingSpam)
        time.sleep(self.waitTimeTillStartingSpam)
        # copyToClipboard(message)
        initialTime = time.time()
        i = 1
        while i <= self.numberOfTextsToSend:
            # pt.hotkey('ctrl', 'v')

            # pt.press("enter")
            print("spammed", i, "th message")
            time.sleep(self.delayTimeBetweenEachTextSent)
            i += 1
            finalTime = time.time()

        print("spammed", self.numberOfTextsToSend, "messages in", finalTime - initialTime)
