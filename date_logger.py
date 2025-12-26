"""

Provides date and time logging functions

"""

from datetime import datetime

def get_timestamp():
    
    """
    
    Returns the current date and time as a formatted string
    
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

test = get_timestamp()
print(f"\nThis is today year month day hour minute and second at this moment: {test}")