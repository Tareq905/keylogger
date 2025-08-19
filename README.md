# Keylogging Simulation & Detection

## Overview

This project demonstrates both **red team** (attacker simulation) and **blue team** (defensive detection) concepts in cybersecurity.
It is designed **for educational and awareness purposes only** and does not perform any malicious actions.

* **Simulation Mode**: Demonstrates how attackers might attempt to gather system information, take screenshots, and log keystrokes (simulated keystrokes only, not real ones).
* **Detection Mode**: Scans running processes to detect suspicious programs that may behave like keyloggers.

This dual approach highlights the importance of understanding both attacker techniques and defensive strategies.

---

## Features

* Collects **system information** (OS, machine, processor, hostname).
* Takes a **screenshot** of the current screen.
* Generates **simulated keystroke logs** (safe, random characters only).
* Detects **suspicious processes** related to keylogging (e.g., `keyboard`, `pynput`).
* Provides a simple **menu-driven interface** to choose between simulation and detection.

---

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/cybersecurity-awareness-tool.git
cd cybersecurity-awareness-tool
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python main.py
```

### 4. Choose an option

* **1** → Run Simulation (fake keylogger + system info + screenshot).
* **2** → Run Detection (scan processes for suspicious keylogger activity).

---

## Example Output

### Simulation

```
OS: Windows
OS Release: 10
OS Version: 10.0.19045
Machine: AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
Hostname: DESKTOP-12345
Screenshot saved as screenshot_2025-08-19_20-30-12.png
Simulated keystrokes:
kd83p0 xz29d lm0q
```

### Detection

```
[*] Scanning for possible keyloggers...

No suspicious processes detected.
```

---

## Requirements

* Python 3.8+
* Libraries: `pyautogui`, `psutil`

Install with:

```bash
pip install pyautogui psutil
```

---

## Ethical Disclaimer

⚠️ This project is intended **solely for educational and awareness purposes**.
It **does not capture real keystrokes** and should **never be modified for malicious use**.
Always use responsibly in controlled environments.

---

## Resume Highlight

> **Cybersecurity Awareness Tool** – Built a Python-based project demonstrating both offensive (simulated keylogging, system profiling, screenshots) and defensive (keylogger detection) techniques. Showcases red team vs blue team approaches for security training and awareness.

---

## License

MIT License – Free to use for learning and awareness projects.
