"""

Provides user activity functions

"""

import random

def pick_random_user():
    """
   
    Returns a randomly selected username
   
    """
    
    users = ["Alice","Bob", "David", "Lucas", "Guadalupe"]
    return random.choice(users)

test = pick_random_user()
print(f"\nRandom name generating is: {test}")