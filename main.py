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
     
     
     
     

while True:
    user_input = input("\
                    -----------------Menu--------------\n \
                    [1]Read              [2]Print DF \n \
                    [3]Print Col         [4]Drop Col\n \
                    [5]Get Col Ct        [6]Get Un. Ct \n \
                    [7]Get First 5                     \n \
                                [c]Clear Console\n \
                                [d]Done\n")

    if user_input == 'd':
        break

    elif user_input == 'c':
        clear_console()

    elif user_input == '1':
        df = pd.read_csv('data.csv')
        df = df.rename(columns=lambda x: x.strip()) #trim whitespace from headers
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) #trim whitespace from cells
        print('CSV file has been read into a pandas dataframe.')

    elif user_input == '2':
        ################# print df #####################
        try:
            print(df.iloc[:, :10].to_string(index=False, justify='left'))
        except NameError:
            print('Dataframe not yet defined. Please read in CSV file first.')

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
    
    elif user_input == '7':
        ################# count unique values in col #####################
        if df.empty:
            print("DataFrame is empty")
            continue
        
        quantity = input("How many rows would you like to see, please input a number from 1 to " +  str(len(df)) + " \n")
        first_five = first_5(df, int(quantity))

        table = Table(title="This is Table")

        for column_headers in df.columns:
            table.add_column(column_headers, justify="right", style="cyan", no_wrap=True)
        
        for values, value_list in enumerate(first_five):
            row = [str(values)] if True else []
            row += [str(x) for x in value_list]
            table.add_row(*row)
        #for values in first_five:
            #table.add_row(str(values))

        console.print(table)

        #print(df.columns.to_list())
        #print("\n") 

        #quantity = input("How many rows would you like to see, please input a number from 1 to " +  str(len(df)) + " \n")

        #first_five = first_5(df, int(quantity))
        #count = 0
        
    else:
        print('Invalid input. Please try again.')