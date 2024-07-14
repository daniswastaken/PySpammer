import pyautogui, time
time.sleep(5)
with open("spam.txt", "r") as f:
    for lines in f:
        pyautogui.typewrite(lines)
        pyautogui.press("enter")