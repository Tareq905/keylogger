import os
import time
import random
import platform
import pyautogui
import psutil

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": platform.node()
    }
    return system_info

def take_screenshot():
    screenshot_path = f"screenshot_{time.strftime('%Y-%m-%d_%H-%M-%S')}.png"
    pyautogui.screenshot(screenshot_path)
    return screenshot_path

def simulate_keylogger(duration=10):
    keys = list("abcdefghijklmnopqrstuvwxyz0123456789 ")
    log = ""
    start = time.time()
    while time.time() - start < duration:
        log += random.choice(keys)
        time.sleep(0.2)
    return log

def detect_keyloggers():
    suspicious = ["keylogger", "pynput", "keyboard", "pyxhook"]
    detected = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            if any(s in pname for s in suspicious):
                detected.append((proc.info['pid'], proc.info['name']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return detected

def run_simulation():
    info = get_system_info()
    for k, v in info.items():
        print(f"{k}: {v}")
    screenshot_file = take_screenshot()
    print(f"Screenshot saved as {screenshot_file}")
    log = simulate_keylogger()
    print(f"Simulated keystrokes:\n{log}")

def run_detection():
    found = detect_keyloggers()
    if found:
        print("\nSuspicious processes found:")
        for pid, name in found:
            print(f" - PID {pid}: {name}")
    else:
        print("\nNo suspicious processes detected.")

def main():
    print("1. Run Simulation (Fake Keylogger + System Info + Screenshot)")
    print("2. Run Detection (Check for Real Keyloggers)")
    choice = input("Choose option: ")
    if choice == "1":
        run_simulation()
    elif choice == "2":
        run_detection()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
