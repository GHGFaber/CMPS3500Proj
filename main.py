import pandas as pd
import time
import datetime

df = pd.DataFrame()
# Function to get current time
def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def count_all_values(df, column):
    count = 0
    for value in df[column]:
        if value == value:
            count =+ 1
    return count

def count_unique_values(df, column):
    unique_values = {}
    for value in df[column]:
        if value in unique_values:
            unique_values[value] += 1
        else:
            unique_values[value] = 1
    return unique_values

def search_by_value(df, column_name, value):
    try:
        # Check if column_name is in df
        if column_name not in df.columns:
            raise ValueError(f"{column_name} is not a column in the DataFrame")
        
        rows = df[df[column_name] == value]
        return rows[column_name]

    except ValueError as ve:
        print("ValueError:", ve)
        return None
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None


def count_unique_values_in_column(df):
    print(f"[{current_time()}] Select column number to count unique values:\n")
    for i, col_name in enumerate(df.columns):
        print(f"{i}: {col_name}")

    column_choice = int(input("Enter an option: "))
    if column_choice < 0 or column_choice >= len(df.columns):
        print("Invalid column number. Please try again.")
        return

    column_name = df.columns[column_choice]
    unique_values = count_unique_values(df, column_name)

    print(f"Unique values in column '{column_name}': {len(unique_values)}")
    print("Value:  Counts:")
    for value, count in unique_values.items():
        print(f"{value}: {count}")



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
    global df
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
    df = pd.read_csv(file_name)
    end_time = time.time()
    
    print(f"[{current_time()}]" + " " + file_choice)
    print(f"[{current_time()}] Total Columns Read: {df.shape[1]}")
    print(f"[{current_time()}] Total Rows Read: {df.shape[0]}\n")
    print("File loaded successfully!")
    print(f"Time to load {round(end_time - start_time, 2)} sec.\n")

# Function to explore data set
def explore_data():
    if df is None:
        print("No data loaded.")
        return
    print("\nExploring Data:")
    print("***************")
    print("(21) List all Columns:")
    print("(22) Drop Columns:")
    print("(23) Describe Columns:")
    print("(24) Search Element in Column:")
    print("(25) Back to Main Menu:")
    choice = input("Enter an option: ")
    print("\n")
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
        print(f"[{current_time()}] Select column number to Describe:\n")
        
        for i, col_name in enumerate(df.columns):
            print(f"{i}: {col_name}")
        print("\n")
        column_choice = int(input("Enter an option: "))
        if column_choice < 0 or column_choice >= len(df.columns):
            print("Invalid column number. Please try again.")
            return explore_data()
        else:
            column_name = df.columns[column_choice]
            start_time = time.time()
            count = count_all_values(df, column_name)
            unique_values = count_unique_values(df, column_name)
            end_time = time.time()
            print(f"\n[{current_time()}] {column_choice}\n")
            print(f"Column {column_choice} stats:")
            print("============")
            print(f"Count: {count}")
            print(f"Unique: {len(unique_values)}")
            print(f"Stats printed succesfully! Time to process is {round(end_time - start_time, 2)} sec.\n ")
            return explore_data()
    elif choice == "24":
        print("(24) Search Element in Column:")
        print("*******************************")
        print("Select column number to perform a search:")
        print(f"[{current_time()}] Enter element to search:\n")
        for i, col_name in enumerate(df.columns):
            print(f"{i}: {col_name}")
        print("\n")
        while True:
            try:
                column_choice = int(input("Enter an option: "))
                if column_choice < 0 or column_choice >= len(df.columns):
                    print("Invalid column number. Please try again.")
                    continue
                column_name = df.columns[column_choice]
                element = input(f"[{current_time()}] Enter element to search: ")
                try:
                    element = df[column_name].dtype.type(element)
                except ValueError:
                    print("Invalid input for the data type of the selected column. Please try again.")
                    return explore_data()
                rows = search_by_value(df, column_name, element)
                if len(rows) > 0:
                    print(f"[{current_time()}] Element found in these rows. ")
                    print(rows)
                else:
                    print(f"[{current_time()}] Element not found.")
                return explore_data()
            except ValueError:
                print("Invalid input for the column number. Please try again.")
            except IndexError:
                print("Invalid input for the column number. Please try again.")
    elif choice == "26":
        print("(26) Count Unique Values in Column:")
        print("************************************")
        count_unique_values_in_column(df)
        print("\n")
        return explore_data()
    elif choice == "25":
        return main_menu()
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
            print("Invalid choice. Please try again.\n")
