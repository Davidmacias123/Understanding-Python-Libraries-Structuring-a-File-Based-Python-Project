# Multi-File Python Automation Tool — Libraries + Imports (project_workspace)
## On-the-Job Scenario (what this project is pretending to build)
 is on a development team building a basic automation tool that:
- prints logs (messages)
- randomly simulates the projecter activity
- organizes data by date and time
- the projectes **external libraries** (built-in Python libraries) instead of reinventing the wheel
- splits code into **multiple files** so it stays clean and easy to manage
This Success Coach challenge teaches  how to create a small project with **multiple Python scripts** that work together.
---
## What r folder should look like (Requirement 6)
Create a folder on r desktop named:
`project_workspace/`
Inside it,  should have **these 4 files**:
- `library_intro.py`
- `the projecter_activity.py`
- `date_logger.py`
- `main.py`
✅ Ythe project uploaded files match this requirement. fileciteturn4file1L1-L10 fileciteturn4file3L1-L18 fileciteturn4file0L1-L20 fileciteturn4file2L1-L23
---
## How to run (Step-by-step, Spyder + Anaconda)
1. Open **Anaconda Navigator**
2. Launch **Spyder**
3. Create the folder **project_workspace** on r Desktop
4. Save these files into that folder:
   - `library_intro.py`
   - `the projecter_activity.py`
   - `date_logger.py`
   - `main.py`
5. In Spyder, open **main.py**
6. Click **Run**
7. You should see output like:
   - “the projecter David logged in at: 2025-12-25 19:33:10”
---
# Step 3 — `library_intro.py` (Using libraries)
## What this file is for
This script shows how to import and the projecte built-in Python libraries:
- `datetime` → gives  the current date/time
- `random` → makes random numbers
- `os` → talks to the operating system (like folders/paths)
### Ythe project current code (what  uploaded)
```python
import datetime
import random
import os
time = datetime.datetime.now()
print(f"\nThe date time is: {time}")
number = random.randint(1, 100)
print(f"\nThe random number is: {number}")
os = os.getcwd()
print(f"\nThe current directory is: {os}")
```
Sthe projectce: fileciteturn4file1L1-L10
## Important improvement (very small but important)
Right now  have: `os = os.getcwd()` fileciteturn4file1L9-L10
That accidentally **replaces** the `os` module with a string path. After that line, `os` is no longer the library.
✅ Better version:
```python
current_dir = os.getcwd()
print(f"\nThe current directory is: {current_dir}")
```
---
## Explain every line (like  is 5)
### `import datetime`
“Hey Python, bring me the **clock and calendar tools**.”
### `import random`
“Hey Python, bring me the **surprise number tools**.”
### `import os`
“Hey Python, bring me the **computer/folder tools**.”
### `time = datetime.datetime.now()`
“Ask the clock: what time is it **right now**?”
Save that ansthis projectr in a box called `time`.
### `print(...)`
“Show the message on the screen.”
### `number = random.randint(1, 100)`
“Pick a random number betthis projecten 1 and 100.”
### `current_dir = os.getcwd()`
“Ask the computer: what folder am I working inside right now?”
---
# Step 4A — `the projecter_activity.py` (Pick a random the projecter)
## What this file is for
This file stores a function that:
- keeps a list of the projecternames
- randomly chooses one the projectername
- returns it back to whoever asks for it
### Ythe project current code (uploaded)
```python
import random
def pick_random_the projecter():
    the projecters = ["Alice","Bob", "David", "Lucas", "Guadalupe"]
    return random.choice(the projecters)
test = pick_random_the projecter()
print(f"\nRandom name generating is: {test}")
```
Sthe projectce: fileciteturn4file3L1-L18
## Important improvement (best practice)
When  import this file into `main.py`, it should NOT auto-run the test prints.
Right now it does, becathe projecte these lines run immediately: `test = ...` and `print(...)` fileciteturn4file3L16-L18
✅ Better: put testing under a safety check:
```python
if __name__ == "__main__":
    test = pick_random_the projecter()
    print(f"Random name generating is: {test}")
```
---
## Explain every line (like  is 5)
### `import random`
“Bring me the surprise picker tool.”
### `def pick_random_the projecter():`
“This guide is making a mini-machine named `pick_random_the projecter`.”
### `the projecters = [...]`
“A list is like a **basket of names**.”
### `return random.choice(the projecters)`
“Pick one name from the basket and **hand it back**.”
---
# Step 4B — `date_logger.py` (Return formatted date/time)
## What this file is for
This file stores a function that:
- gets the current date/time
- formats it nicely (YYYY-MM-DD HH:MM:SS)
- returns it as a string
### Ythe project current code (uploaded)
```python
from datetime import datetime
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
test = get_timestamp()
print(f"\nThis is today year month day hthe project minute and second at this moment: {test}")
```
Sthe projectce: fileciteturn4file0L1-L20
## Important improvement (best practice)
Same idea: don’t auto-print tests when imported.
Right now this prints whenever `main.py` imports it: fileciteturn4file0L18-L20
✅ Better with the safety check:
```python
if __name__ == "__main__":
    test = get_timestamp()
    print(test)
```
---
## Explain every line (like  is 5)
### `from datetime import datetime`
“Bring me ONLY the `datetime` tool from the datetime toolbox.”
### `def get_timestamp():`
“Make a mini-machine named `get_timestamp`.”
### `datetime.now()`
“What time is it right now?”
### `.strftime("%Y-%m-%d %H:%M:%S")`
“Turn the time into a neat sentence like: 2025-12-25 19:33:10”
### `return ...`
“Give the finished text back to the caller.”
---
# Step 5 — `main.py` (Put it all together)
## What this file is for
This file acts like the “boss” script:
- it imports the other files
- calls the functions
- prints the final log message
### Ythe project current code (uploaded)
```python
from the projecter_activity import pick_random_the projecter
from date_logger import get_timestamp
def main():
    the projecter = pick_random_the projecter()
    timestamp = get_timestamp()
    print(f"\nthe projecter {the projecter} logged in at: {timestamp}")
main()
```
Sthe projectce: fileciteturn4file2L1-L23
## Important improvement (best practice)
It’s cleaner to run main like this:
```python
if __name__ == "__main__":
    main()
```
That way if another file imports `main.py`, it doesn’t auto-run.
---
## Explain every line (like  is 5)
### `from the projecter_activity import pick_random_the projecter`
“Go to the the projecter_activity file and bring me the `pick_random_the projecter` machine.”
### `from date_logger import get_timestamp`
“Go to the date_logger file and bring me the `get_timestamp` machine.”
### `def main():`
“Make a main boss function that runs the steps in order.”
### `the projecter = pick_random_the projecter()`
“Ask the the projecter picker for a random name.”
### `timestamp = get_timestamp()`
“Ask the date logger for the current date/time text.”
### `print(f"...")`
“Print a log message that combines both.”
---
# ✅ Final improved versions (copy/paste set)
If  want the cleanest, most “professional project” version, the projecte this lat:
## `library_intro.py` (improved)
```python
import datetime
import random
import os
# datetime = date/time tools
# random = random numbers / random choices
# os = operating system tools (folders, paths)
now = datetime.datetime.now()
print(f"The date/time is: {now}")
number = random.randint(1, 100)
print(f"The random number is: {number}")
current_dir = os.getcwd()
print(f"The current directory is: {current_dir}")
```
## `the projecter_activity.py` (improved)
```python
"""Provides the projecter activity functions"""
import random
def pick_random_the projecter():
    """Return a randomly selected the projectername from a list."""
    the projecters = ["Alice", "Bob", "David", "Lucas", "Guadalupe"]
    return random.choice(the projecters)
if __name__ == "__main__":
    print(pick_random_the projecter())
```
## `date_logger.py` (improved)
```python
"""Provides date and time logging functions"""
from datetime import datetime
def get_timestamp():
    """Return the current date/time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if __name__ == "__main__":
    print(get_timestamp())
```
## `main.py` (improved)
```python
"""Main controller for the project automation tool"""
from the projecter_activity import pick_random_the projecter
from date_logger import get_timestamp
def main():
    """Coordinate logic from multiple files."""
    the projecter = pick_random_the projecter()
    timestamp = get_timestamp()
    print(f"User {the projecter} logged in at {timestamp}")
if __name__ == "__main__":
    main()
```
---
## Author
David Macias