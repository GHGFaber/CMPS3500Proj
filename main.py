import pandas as pd
import time
import datetime

# Function to get current time
def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to display main menu
def main_menu():
    print("Main Menu:")
    print("**********")
    print("(1) Load Data")
    print("(2) Exploring Data")
    print("(3) Data Analysis")
    print("(4) Print Data Set")
    print("(5) Quit")

# Function to load data set
def load_data():
    global data
    print("Load data set:")
    print("**************")
    print(f"[{current_time()}] Select the number of the file to load from the list below:")
    print("[1] data.csv")
    print("[2] main.py")
    print("[3] nothing.csv")
    file_choice = input()
    # Select correct file based on user input 
    if file_choice == "1":
        file_name = "data.csv"
    elif file_choice == "2":
        file_name = "main.py"
    elif file_choice == "3":
        file_name = "nothing.csv"
    else:
        print("Invalid choice. Returning to the main menu.")
        return

    # Load data set and time how long it takes
    start_time = time.time()
    data = pd.read_csv(file_name)
    end_time = time.time()
    
    print(f"[{current_time()}]" + " " + file_choice)
    print(f"[{current_time()}] Total Columns Read: {data.shape[1]}")
    print(f"[{current_time()}] Total Rows Read: {data.shape[0]}\n")
    print("File loaded successfully!")
    print(f"Time to load {round(end_time - start_time, 2)} sec.\n")

# Function to explore data set
def explore_data():
    print("\nExploring Data:")
    print("***************")
    print("(21) List all Columns:")
    print("(22) Drop Columns:")
    print("(23) Describe Columns:")
    print("(24) Search Element in Column:")
    print("(25) Back to Main Menu:")
    choice = input("Enter an option: ")
    if choice == "21":
        print("(21) List of all columns:")
        print("*************************")
    elif choice == "22":
        print("(22) Drop Columns:")
        print("******************")
        print("Select a column number to drop:")        
    elif choice == "23":
        print("(23) Describe Columns:")
        print("**********************")
        print("Select column number to Describe:")
    elif choice == "24":
        print("(24) Search Element in Column:")
        print("*******************************")
        print("Select column number to perform a search:")
    elif choice == "25":
        return
    else:
        print("Invalid choice. Please try again.")
        explore_data()

def data_analysis():
    print("\nData Analysis:")
    print("**************")
    return

def print_data():
    pass

# Main loop
if __name__ == "__main__":
    while True:
        # Display main menu
        main_menu()
        choice = input("Enter an option: ")
        # Call function based on user input
        if choice == "1":
            load_data()
        elif choice == "2":
            explore_data()
        elif choice == "3":
            data_analysis()
        elif choice == "4":
            print_data()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
