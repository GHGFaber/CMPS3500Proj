import pandas as pd
import os
import time
from time import sleep
import datetime

# Function to get current time
def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to clear termainal screen
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Function to pause program until user input
def wait_on_user():
    while True:
        user_input = input("\nEnter 'c' to continue: ")
        if user_input == 'c':
            break

    clear_console() # Clear console