# Multi-File Python Automation Tool — Libraries + Imports

This project shows how to:
- use built-in Python libraries (`datetime`, `random`, `os`)
- split code into multiple files (modules)
- import functions from other files
- print a log message like: **`User [NAME] logged in at [DATE_TIME]`**

---

## Folder Setup (Required)
Create a folder on the Desktop named:

`project_workspace`

Inside `project_workspace`, create **exactly these files**:

- `library_intro.py`
- `user_activity.py`
- `date_logger.py`
- `main.py`

**Important:** All four files must be in the **same folder**.

---

## How to Run in Spyder (Step-by-step)
1. Open **Anaconda Navigator**
2. Launch **Spyder**
3. Save the four files inside the Desktop folder: `project_workspace`
4. In Spyder, set the working directory to that folder:
   - In the top toolbar, change the working directory to `.../Desktop/project_workspace`
   - (If the working directory is wrong, imports may fail with `ModuleNotFoundError`.)
5. Open `main.py`
6. Click **Run**

Expected output (example):
- `User Alice logged in at 2025-12-25 19:33:10`

---

# Step 3 — `library_intro.py` (Using libraries)

## What each library is used for
- **datetime**: gets today’s date/time (calendar + clock)
- **random**: generates random numbers and random choices
- **os**: reads system/OS information like the current folder path

## Correct code (copy/paste)
```python
"""library_intro.py
Intro to built-in Python libraries used for simple automation tasks.
"""

import datetime   # date/time tools
import random     # random numbers and random selection
import os         # operating system tools (paths, folders)

# A) Print today's date
today = datetime.date.today()
print(f"Today's date is: {today}")

# B) Random number between 1 and 100
number = random.randint(1, 100)
print(f"Random number (1-100): {number}")

# C) Print current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")
```

### Common error to avoid
❌ Do **not** do this:
```python
os = os.getcwd()
```
That line replaces the `os` library with a string, which breaks future `os` usage.

---

# Step 4A — `user_activity.py` (Random user picker)

## Requirement
Define a function that randomly picks a user from a list and **returns** the name.

## Correct code (copy/paste)
```python
"""user_activity.py
Functions that simulate user activity.
"""

import random

def pick_random_user():
    """Return a randomly selected username from a predefined list."""
    users = ["Alice", "Bob", "David", "Lucas", "Guadalupe"]
    return random.choice(users)

# Optional test (runs only if this file is executed directly)
if __name__ == "__main__":
    print(pick_random_user())
```

---

# Step 4B — `date_logger.py` (Timestamp generator)

## Requirement
Define a function that returns the current date and time formatted as a string.

## Correct code (copy/paste)
```python
"""date_logger.py
Functions that create formatted timestamps for logging.
"""

from datetime import datetime

def get_timestamp():
    """Return the current date/time formatted as YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Optional test (runs only if this file is executed directly)
if __name__ == "__main__":
    print(get_timestamp())
```

---

# Step 5 — `main.py` (Combine modules + print log)

## Requirement
- Import `user_activity` and `date_logger`
- Call their functions
- Print: `User [NAME] logged in at [DATE_TIME]`

## Correct code (copy/paste)
```python
"""main.py
Main script that coordinates the automation tool across multiple files.
"""

from user_activity import pick_random_user
from date_logger import get_timestamp

def main():
    """Print a log message showing a random user login and the current timestamp."""
    name = pick_random_user()
    timestamp = get_timestamp()
    print(f"User {name} logged in at {timestamp}")

if __name__ == "__main__":
    main()
```

---

## Explain Like You’re 5 (super simple)

### Big idea
This project is like a small team of helpers:

- **library_intro.py** = the helper that shows the date, a random number, and the current folder  
- **user_activity.py** = the helper that picks a random name  
- **date_logger.py** = the helper that tells the current date/time in a neat format  
- **main.py** = the boss that asks the helpers for info and prints the final message

---

## Explain every line (breakdown)

### 1) `import ...`
`import datetime`, `import random`, `import os`  
These lines mean: “Bring in extra tools.”

### 2) `def function_name():`
`def` means: “Create a reusable mini-program (a function).”

### 3) `return ...`
`return` means: “Give the result back.”

### 4) `from file import function`
This means: “Go to another file in the same folder and bring in a function.”

### 5) `if __name__ == "__main__":`
This means: “Only run the test code when this file is run directly (not when imported).”
This prevents accidental extra prints when `main.py` imports the other files.

---

## Troubleshooting (Fixes most GitHub/Spyder errors)

### Error: `ModuleNotFoundError: No module named 'user_activity'`
Fix:
- Ensure `main.py`, `user_activity.py`, `date_logger.py` are in the **same folder**
- Set Spyder working directory to the folder: `project_workspace`

### Error: extra prints happen before the main log
Fix:
- Keep test prints under:
  - `if __name__ == "__main__":`

### Error: `AttributeError` with `os`
Fix:
- Do not overwrite the `os` module with a variable named `os`
- Use `current_dir = os.getcwd()` instead

---

## Author
David Macias
