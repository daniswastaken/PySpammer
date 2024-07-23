import pyautogui, time
time.sleep(5)
with open("bang.txt", "r") as f:
    for lines in f:
        pyautogui.typewrite(lines)
        pyautogui.press("enter")