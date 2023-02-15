import pyautogui as pt
import pyperclip as clipboard
import time

# limit = input("Enter limit:")
# message = input("Enter message:")
message2 = "Testing text abc"
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

i = 0
time.sleep(15)

limit = 50
initalTime = time.time()

clipboard.copy(message2)

while i < limit:
    # pt.write(message)
    # pt.typewrite(message)

    pt.hotkey('ctrl', 'v')

    pt.press("enter")
    print("spammed", i, "th message")
    time.sleep(0.5)

    # the message is written where -
    # the cursor belongs

    i += 1

finalTime = time.time()

print("spammed ", limit, "messages in ", finalTime - initalTime)
