import time
import pyautogui
delay = input("delay")
input("pense à copier la personne à spam")
time.sleep(int(delay))
i = 0
while True:
    pyautogui.hotkey("ctrl","v")
    pyautogui.hotkey("space","enter",interval=0.2)
    i += 1
    if i == 10:
        time.sleep(30)
        i = 0