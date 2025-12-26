import datetime
import random
import os

time = datetime.datetime.now()
print(f"\nThe date time is: {time}")

number = random.randint(1, 100)
print(f"\nThe random number is: {number}")

os = os.getcwd()
print(f"\nThe current directory is: {os}")
