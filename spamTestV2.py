import pyautogui as pt
import pyperclip as clipboard
import time

# limit = input("Enter limit:")
# message = input("Enter message:")
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

limit = 500
initalTime = time.time()
while i < limit:
    # pt.write(message)
    #pt.typewrite(message)
    clipboard.copy(message)
    pt.hotkey('ctrl', 'v')
    clipboard.copy('')
    # the message is written where -
    # the cursor belongs

    pt.press("enter")
    print("spammed", i, "th message")

    i += 1

finalTime = time.time()

print("spammed ", limit, "messages in ", finalTime - initalTime)
