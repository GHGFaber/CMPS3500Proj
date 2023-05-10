import pandas as pd
import time
import util
import explore
import describe

# Function to display main menu
def main_menu():
    util.clear_console()
    print("Main Menu:")
    print("**********")
    print("(1) Load Data")
    print("(2) Exploring Data")
    print("(3) Data Analysis")
    print("(4) Print Data Set")
    print("(5) Quit")

# Function to load data set
def load_data():
    util.clear_console()
    global df
    print("Load data set:")
    print("**************")
    print(f"[{util.current_time()}] Select the number of the file to load from the list below:")
    print("\tPlease select an option:")
    print("\t[1] data.csv")
    print("\t[2] Crime_Data_from_2017_to_2019.csv")
    print("\t[3] nothing.csv")
    file_choice = input()
    if file_choice == "1":
        file_name = "data.csv"
    elif file_choice == "2":
        file_name = "Crime_Data_from_2017_to_2019.csv"
    elif file_choice == "3":
        file_name = "nothing.csv"
    else:
        print("Invalid choice. Returning to the main menu.")
        return

    try:
        start_time = time.time()
        df = pd.read_csv(file_name)
        end_time = time.time()
        df = df.rename(columns=lambda x: x.strip()) #trim whitespace from headers
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) #trim whitespace from cells    
    except FileNotFoundError:
        print("File not found.")
        util.wait_on_user()
        return

    print("")
    print(f"[{util.current_time()}]" + " " + file_choice)
    print(f"[{util.current_time()}] Total Columns Read: {df.shape[1]}")
    print(f"[{util.current_time()}] Total Rows Read: {df.shape[0]}\n")
    print("File loaded successfully!")
    print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    util.wait_on_user()

# Function to explore data set
def explore_data():
    util.clear_console()
    print("Exploring Data:")
    print("***************")
    print("(21) List all Columns:")
    print("(22) Drop Columns:")
    print("(23) Describe Columns:")
    print("(24) Search Element in Column:")
    print("(25) Back to Main Menu:")
    choice = input("Enter an option: ")
    util.clear_console()

    if choice == "21":
        print("(21) List of all columns:")
        print("*************************")
        explore.list_all_columns(df)
    
    elif choice == "22":
        print("(22) Drop Columns:")
        print("******************")
        explore.drop_column(df)

    elif choice == "23":
        print("(23) Describe Columns:")
        print("**********************")
        describe_data()

    elif choice == "24":
        print("(24) Search Element in Column:")
        print("*******************************")
        print("Select column number to perform a search:")
        #TODO: Implement search

    elif choice == "25":
        return
    
    else:
        print("Invalid choice. Please try again.")
        explore_data()

    # Loop back to current menu
    explore_data()

# Function to describe data set
def describe_data():
    util.clear_console()
    print("Describing Data:")
    print("***************")
    print("(231) Count:")
    print("(232) Unique Count:")
    print("(233) Mean:")
    print("(234) Median:")
    print("(235) Mode:")
    print("(236) Standard Deviation:")
    print("(237) Variance:")
    print("(238) Minimum:")
    print("(239) Maximum:")
    print("( b ) prev menu:")
    choice = input("Enter an option: ")
    if choice == "231":
        util.clear_console()
        print("(231) Count:")
        print("*************************")

    elif choice == "232":
        util.clear_console()
        print("(232) Unique Count:")
        print("******************")

    elif choice == "233":
        util.clear_console()
        print("(233) Mean:")
        print("**********************")
        describe.get_mean(df)

    elif choice == "234":
        util.clear_console()
        print("(234) Median:")
        print("*******************************")
        describe.get_median(df)

    elif choice == "235":
        util.clear_console()
        print("(235) Mode:")
        print("*******************************")
        describe.get_mode(df)

    elif choice == "236":
        util.clear_console()
        print("(236) Standard Deviation:")
        print("*******************************")

    elif choice == "237":
        util.clear_console()
        print("(237) Variance:")
        print("*******************************")

    elif choice == "238":
        util.clear_console()
        print("(238) Minimum:")
        print("*******************************")

    elif choice == "239":
        util.clear_console()
        print("(239) Maximum:")
        print("*******************************")

    elif choice == "b":
        return
    
    else:
        print("Invalid choice. Please try again.")
        describe_data()
    
    util.wait_on_user()
    
    

def data_analysis():
    util.clear_console()
    print("\nData Analysis:")
    print("**************")
    return

def print_data():
    try:
        print(df.to_string(index=False))
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
        print("Error occurred:", e)
    util.wait_on_user()

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
