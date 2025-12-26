"""

Main controller for our automatic tool

"""

from user_activity import pick_random_user
from date_logger import get_timestamp

def main():
    
    """
    
    Coordinate logic from multiple files
    
    """

    user = pick_random_user()
    timestamp = get_timestamp()
    print(f"\nuser {user} logged in at: {timestamp}")
    
main()
