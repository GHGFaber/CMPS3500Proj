# Course: CMPS3500
# Class Project - PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# Date: 04/08/2023
# Project Members:
#
#   - Moises Fuentes Rivera
#   - Douglas Rank
#   - Christopher Ramirez
#   - Justin Ulloa
#
# Description: Menu UI

import pandas as pd
import os
import time
import datetime

from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()
df = pd.DataFrame()

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def count_unique_values(df, column):
    unique_values = {}
    for value in df[column]:
        if value in unique_values:
            unique_values[value] += 1
        else:
            unique_values[value] = 1
    return unique_values

def count_all_values(df, column):
    count = 0
    for value in df[column]:
        count+=1
    return count


#!!!!!!!!!!!    Moises' "first few" function   

def first_5(df, quantity):
    first_5 = []
    first_5 = df.head(quantity).values.tolist()
    return first_5

# Function to get current time
def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def menuDisplay():
    print ("\
                    -----------------Menu--------------------- \n \
                    [1]Load Data             [2]Exploring Data \n \
                    [3]Data Analysis         [4]Print Data Set\n \
                                [c]Clear Console\n \
                                [d]Done\n")

def load_data():
    global df
    print ("\
                    -----------------Load Data Set--------------\n \
                    [1]data.csv                                 \n \
                    [2]N/A                                      \n \
                    [3]N/A                                      \n \
                                [c]Clear Console\n \
                                [d]Done\n")
    file_choice = input(f"[{current_time()}] Select the number of the file to load from the list below: ")
    if file_choice == "1":
        file_name = "data.csv"
        # Load data set and time how long it takes
        start_time = time.time()
        df = pd.read_csv(file_name)
        df = df.rename(columns=lambda x: x.strip()) #trim whitespace from headers
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) #trim whitespace from cells
        print('CSV file has been read into a pandas dataframe.')
        end_time = time.time()
        
        print(f"[{current_time()}]" + " " + file_name)
        print(f"[{current_time()}] Total Columns Read: {df.shape[1]}")
        print(f"[{current_time()}] Total Rows Read: {df.shape[0]}\n")
        print("File loaded successfully!")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    else:
        print("Invalid choice. Returning to the main menu.")
        return
    
def print_data():
################# count unique values in col #####################
    if df.empty:
        print("DataFrame is empty")
        return
    
    quantity = input("How many rows would you like to see, please input a number from 1 to " +  str(len(df)) + " \n")
    first_five = first_5(df, int(quantity))

    table = Table(title="This is Table")

    for column_headers in df.columns:
        table.add_column(column_headers, justify="right", style="cyan", overflow="fold")
    
    for values, value_list in enumerate(first_five):
        row = [str(values)] if True else []
        row += [str(x) for x in value_list]
        table.add_row(*row)

    console.print(table) 

"""while True:
    user_input = input("\
                    -----------------Menu--------------\n \
                    [1]Load Data             [2]Exploring Data \n \
                    [3]Data Analysis         [4]Print Data Set\n \
                                [c]Clear Console\n \
                                [d]Done\n")

    elif user_input == '3':
        ################# print col #####################
        if df.empty:
            print("DataFrame is empty")
            continue

        print(df.columns.to_list())
        col_name = input("Column name:  ")
        
        if col_name not in df.columns:
            print("Error: Column name does not exist in dataframe")
            continue
        
        print(df[col_name])

    elif user_input == '4':
        ################# delete col #####################
        if df.empty:
            print("DataFrame is empty")
            continue

        print(df.columns.to_list())
        col_name = input("Column name:  ")
        
        if col_name not in df.columns:
            print("Error: Column name does not exist in dataframe")
            continue
        
        df = df.drop(col_name, axis=1)

        if col_name not in df.columns:
            print(f'Column [ "{col_name}" ] dropped from dataframe')
        else:
            print(f'Error dropping column [ "{col_name}" ] from dataframe')

    elif user_input == '5':
        ################# count unique values in col #####################
        if df.empty:
            print("DataFrame is empty")
            continue

        print(df.columns.to_list())
        col_name = input("Column name:  ")
        
        if col_name not in df.columns:
            print("Error: Column name does not exist in dataframe")
            continue
        
        col_count = count_all_values(df, col_name)
        print(col_count)

    elif user_input == '6':
        ################# count unique values in col #####################
        if df.empty:
            print("DataFrame is empty")
            continue

        print(df.columns.to_list())
        col_name = input("Column name:  ")
        
        if col_name not in df.columns:
            print("Error: Column name does not exist in dataframe")
            continue
        
        unique_col_count = count_unique_values(df, col_name)
        print(len(unique_col_count))

        """
if __name__ == "__main__":
    while True:
        # Display Main Menu
        menuDisplay()
        user_input = input("Enter an option: ")
        if user_input == "d":
            break
        elif user_input == "1": 
            load_data()
        elif user_input == "2": 
            explore_data()
        elif user_input == "3": 
            data_analysis()
        elif user_input == "4": 
            print_data()
        elif user_input == "c": 
            clear_console()
        else:
            print("Invalid Choice. Please Try Again.")