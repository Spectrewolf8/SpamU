import pyautogui as pt
import pyperclip as clipboard
import time

# limit = input("Enter limit:")
# message = input("Enter message:")
message2 = "y"
message = """Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?
Test paragraph abcdefghijklmnopqrstuvwxyz1234567890!$%^&&****((((()_+{}[]"'||.>,</?"""

i = 1

waitTimeTillStaringSpam = 15

numberOfTextsToSend = 10


delayTimeBetweenEachTextSent = 1

time.sleep(waitTimeTillStaringSpam)
initialTime = time.time()
clipboard.copy(message2)

while i <= numberOfTextsToSend:
    # pt.write(message)
    # pt.typewrite(message)

    pt.hotkey('ctrl', 'v')

    pt.press("enter")
    print("spammed", i, "th message")
    time.sleep(delayTimeBetweenEachTextSent)

    # the message is written where -
    # the cursor belongs

    i += 1

finalTime = time.time()

print("spammed", numberOfTextsToSend, "messages in", finalTime - initialTime)
