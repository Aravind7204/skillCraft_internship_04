# 🖨️ Basic Keylogger Tool (Python)

A simple **keylogger tool** developed using **Python** and the `pynput` library. This program records and logs all the keystrokes pressed on the keyboard and saves them to a **log file** for review.

> **⚠️ Ethical Disclaimer**  
> This project is intended **solely for educational purposes** and to demonstrate how keylogging works. Do not use this tool for any malicious or unethical activities. Always get **explicit permission** from users before running keyloggers on their systems.  
> **Unauthorized keylogging is illegal** and unethical.

---

## 📝 About the Project

This project captures **keyboard events** and records them into a `.txt` file. It listens for both **character keys** (letters, numbers) and **special keys** (Enter, Space, Backspace, etc.). The tool is lightweight, runs silently in the background, and provides a basic understanding of how **keystroke logging** works.

---

## 💡 Features
✅ Logs every keystroke to a text file  
✅ Detects **special keys** (Enter, Space, Tab, etc.)  
✅ Runs continuously in the background  
✅ Easily customizable and extendable  
✅ Educational tool to demonstrate **keyboard listeners** in Python  

---

## 🛠️ Technologies Used
- **Python 3.x**  
- **pynput** (for capturing keyboard events)

---

## 📂 Project Structure
```
basic-keylogger/
│
├── keylogger.py        # Main keylogger script
├── key_log.txt         # File where keystrokes are saved
└── README.md           # Project documentation
```

---

## 🚀 How It Works

### Key Functionalities:
- **Logs all keystrokes** typed on the keyboard.
- Saves keystrokes in a plain text file (`key_log.txt`).
- Special keys like `[ENTER]`, `[SPACE]`, and `[BACKSPACE]` are clearly labeled.
- Runs until the program is manually stopped (or you can add a key to stop it, like `ESC`).

### Example Log Output:
```
hello [SPACE] world [ENTER]
password123 [BACKSPACE] 4
```

---

## ▶️ How to Run

### Prerequisites:
- Python 3.x installed  
- Install the `pynput` library:
  ```bash
  pip install pynput
  ```

### Run the Script:
1. Clone this repository or download the `keylogger.py` file.
2. Run the script:
   ```bash
   python keylogger.py
   ```
3. All keystrokes will be saved in the file `key_log.txt` in the same directory.

---

## 📌 Important Notes
- To **stop** the script manually, press `Ctrl + C` in the terminal or close the terminal window.  
- Optionally, you can modify the `on_release()` function to stop the listener when a specific key (like `ESC`) is pressed.

```python
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stops the listener
```

---

## ⚠️ Disclaimer & Ethics
This project is for **learning and ethical hacking education**. Unauthorized use of keyloggers may violate **privacy laws** and **terms of service agreements**. Always:
- Get **permission** from the device owner before running keyloggers.
- Use responsibly and **never** for unethical purposes.

---

## 📄 License
This project is free to use for **ethical hacking practice** and **educational purposes**.

---
